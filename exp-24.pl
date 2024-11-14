disease(diabetes, avoid(sugar)).
disease(diabetes, avoid(fat)).
disease(hypertension, avoid(salt)).
disease(hypertension, avoid(fat)).
disease(obesity, avoid(sugar)).
disease(obesity, avoid(fat)).
disease(heart_disease, avoid(salt)).
disease(heart_disease, avoid(fat)).
food(apple, sugar, low).
food(apple, fat, low).
food(apple, salt, low).
food(burger, sugar, high).
food(burger, fat, high).
food(burger, salt, high).
food(salad, sugar, low).
food(salad, fat, low).
food(salad, salt, low).
food(chips, sugar, low).
food(chips, fat, high).
food(chips, salt, high).
suggest_food(Disease, Food):-
    disease(Disease, avoid(Ingrediant)),
    food(Food, Ingrediant, low).
avoid_food(Disease, Food):-
    disease(Disease, avoid(Ingrediant)),
    food(Food, Ingrediant, high).
