ITEMS_DICT = {
    'signalment_physical': [
        'age', 'breed', 'gender', 'neuter_status', 'vomit_nausea',
        'lethargy_weakness', 'appetite_loss', 'diarrhea_melena',
        'abdominal_pain', 'weight_loss', 'duration', 'bw', 'temp',
        'hr', 'rr', 'bcs', 'hydration_status'
    ],
    'cbc': [
        'wbc', 'red_blood_cell_count', 'hemoglobin', 'packed_cell_volume',
        'mean_corpuscular_volume', 'mean_corpuscular_hemoglobin_concentration',
        'plasma_protein', 'platelet_count', 'absolute_neutrophil',
        'absolute_bands', 'absolute_lymphocyte', 'absolute_monocyte',
        'absolute_eosinophil', 'absolute_basophil', 'absolute_other'
    ],
    'chem': [
        'glucose', 'lactic_acid', 'blood_urea_nitrogen', 'creatinine',
        'sodium', 'potassium', 'enzymatic_carbon_dioxide', 'chloride',
        'anion_gap_calculated', 'calcium', 'phosphorus', 'magnesium',
        'total_protein', 'albumin', 'globulin', 'total_bilirubin',
        'gamma_glutamyltransferase', 'alanine_aminotransferase',
        'alkaline_phosphatase', 'cholesterol'
    ],
    'cpli': ['spec_cpli'],
    'aus': [
        'size', 'echogenecity_of_pancreatic_parenchyma',
        'echogenecity_of_peripancreatic_mesentery', 'pancreatic_echotexture',
        'free_fluid_effusion', 'conclusions'
    ]
}