class HealthAnalytics:

    def generate(self, dashboard):

        tests = dashboard.get("tests", [])

        total = len(tests)

        normal = 0
        abnormal = 0
        critical = 0

        for test in tests:

            status = str(
                test.get(
                    "status",
                    ""
                )
            ).lower()

            severity = str(
                test.get(
                    "severity",
                    ""
                )
            ).lower()

            if status == "normal":

                normal += 1

            else:

                abnormal += 1

            if severity in [
                "high",
                "critical",
                "severe"
            ]:

                critical += 1

        return {

            "total_tests": total,

            "normal_tests": normal,

            "abnormal_tests": abnormal,

            "critical_tests": critical

        }


health_analytics = HealthAnalytics()