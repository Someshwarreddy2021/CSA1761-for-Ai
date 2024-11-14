% Facts: Symptoms associated with various diseases.
% disease(Disease, Symptom).
disease(flu, fever).
disease(flu, chills).
disease(flu, headache).
disease(flu, sore_throat).
disease(flu, cough).

disease(cold, cough).
disease(cold, sneezing).
disease(cold, sore_throat).
disease(cold, runny_nose).

disease(covid, fever).
disease(covid, dry_cough).
disease(covid, shortness_of_breath).
disease(covid, fatigue).
disease(covid, loss_of_taste_smell).

disease(allergy, sneezing).
disease(allergy, runny_nose).
disease(allergy, itchy_eyes).
disease(allergy, rash).

disease(asthma, shortness_of_breath).
disease(asthma, chest_tightness).
disease(asthma, wheezing).
disease(asthma, cough).

disease(pneumonia, fever).
disease(pneumonia, cough).
disease(pneumonia, chest_pain).
disease(pneumonia, shortness_of_breath).

% Diagnosis rule: Suggests a disease based on symptoms.
% diagnosis(Disease, Symptoms)
diagnosis(Disease, Symptoms) :-
    disease(Disease, Symptom),
    member(Symptom, Symptoms).

% Helper rule to find all possible diagnoses based on a list of symptoms
% This uses findall to collect all diseases that match the provided symptoms.
possible_diagnoses(Symptoms, Diagnoses) :-
    findall(Disease, diagnosis(Disease, Symptoms), DiagnosesList),
    sort(DiagnosesList, Diagnoses).  % Removes duplicates
