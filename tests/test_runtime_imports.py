import sys
import types
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


@pytest.fixture
def fake_streamlit(monkeypatch):
    class FakeSessionState(dict):
        def __getattr__(self, name):
            return self[name]

        def __setattr__(self, name, value):
            self[name] = value

    state = FakeSessionState()
    st = types.SimpleNamespace(
        session_state=state,
        set_page_config=lambda **kwargs: None,
        title=lambda *args, **kwargs: None,
        write=lambda *args, **kwargs: None,
        rerun=lambda: None,
    )
    monkeypatch.setitem(sys.modules, "streamlit", st)
    return st, state


def test_frontend_app_imports_with_frontend_views(monkeypatch, fake_streamlit):
    for module_name in [
        "frontend.views.welcome",
        "frontend.views.login",
        "frontend.views.register",
        "frontend.views.dashboard",
    ]:
        module = types.ModuleType(module_name)
        module.render_welcome = lambda: None
        module.render_login = lambda: None
        module.render_register = lambda: None
        module.render_dashboard = lambda: None
        monkeypatch.setitem(sys.modules, module_name, module)

    sys.modules.pop("frontend.app", None)

    import frontend.app as frontend_app

    assert frontend_app is not None


def test_frontend_app_routes_authenticated_users_to_dashboard(monkeypatch, fake_streamlit):
    render_calls = []

    welcome_module = types.ModuleType("frontend.views.welcome")
    welcome_module.render_welcome = lambda: render_calls.append("welcome")

    login_module = types.ModuleType("frontend.views.login")
    login_module.render_login = lambda: render_calls.append("login")

    register_module = types.ModuleType("frontend.views.register")
    register_module.render_register = lambda: render_calls.append("register")

    dashboard_module = types.ModuleType("frontend.views.dashboard")
    dashboard_module.render_dashboard = lambda: render_calls.append("dashboard")

    session_memory_module = types.ModuleType("memory.session_memory")
    session_memory_module.session_memory = types.SimpleNamespace(initialize=lambda: None)

    for module_name, module in {
        "frontend.views.welcome": welcome_module,
        "frontend.views.login": login_module,
        "frontend.views.register": register_module,
        "frontend.views.dashboard": dashboard_module,
        "memory.session_memory": session_memory_module,
    }.items():
        monkeypatch.setitem(sys.modules, module_name, module)

    fake_streamlit[1]["page"] = "login"
    fake_streamlit[1]["logged_in"] = True

    sys.modules.pop("frontend.app", None)

    import frontend.app as frontend_app

    assert frontend_app is not None
    assert render_calls == ["dashboard"]


def test_session_controller_new_chat_resets_conversation(monkeypatch, fake_streamlit):
    import controllers.session_controller as session_controller_module

    monkeypatch.setattr(
        session_controller_module.database,
        "create_chat_session",
        lambda **kwargs: "session-123",
    )
    monkeypatch.setattr(session_controller_module.session_memory, "clear_report", lambda: None)
    monkeypatch.setattr(session_controller_module.session_memory, "clear_image", lambda: None)

    fake_streamlit[1]["conversation_context"] = [{"role": "assistant", "content": "old"}]

    session_id = session_controller_module.session_controller.new_chat("user-1")

    assert session_id == "session-123"
    assert fake_streamlit[1]["conversation_context"] == []
