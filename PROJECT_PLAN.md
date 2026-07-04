# Multi-Agent Patient Triage & SOAP Note Generation System

## Objective
Convert doctor-patient conversations into structured SOAP Notes using multiple AI agents.

## Input
- Audio file (.mp3/.wav)
OR
- Text transcript

## Output
- SOAP Note
- Drug Interaction Warnings
- Safety Review Report

## Agents

### Agent 1: Transcription Agent
Input: Audio
Output: Transcript

### Agent 2: Symptom Extraction Agent
Input: Transcript
Output:
- Symptoms
- Duration
- Medications
- Allergies

### Agent 3: Medical RAG Agent
Input: Symptoms
Output:
- Relevant medical knowledge

### Agent 4: Drug Interaction Agent
Input: Medications
Output:
- Interaction warnings

### Agent 5: SOAP Generator Agent
Input: All previous outputs
Output:
- SOAP Note

### Agent 6: Clinical Safety Agent
Input: SOAP Note
Output:
- Errors
- Missing information
- Safety warnings

## Workflow

Symptom Agent

↓

Memory Update

↓

RAG

↓

Risk

↓

Drug

↓

SOAP

↓

Safety

↓

Guardrail

↓

Final Response