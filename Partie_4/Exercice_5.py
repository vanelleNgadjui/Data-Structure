# <==================== EXERCICE 5: Liste d'emplois ====================>



# Fonction qui prend en entrée une liste de dictionnaires qui représentent les emplois "jobs" et les inputs utilisateurs "user_input"

def search_jobs(jobs, user_input):
    matching_jobs = []
    for job in jobs:
        for key, value in job.items():
            if key != 'id': # clés des dictionnaires
                if isinstance(value, list):
                    for item in value:
                        if user_input.lower() in item.lower() and job not in matching_jobs:
                            matching_jobs.append(job)
                            break
                else:
                    if user_input.lower() in value.lower() and job not in matching_jobs:
                        matching_jobs.append(job)
                        break
    return matching_jobs



# Liste des jobs à afficher pour la fonction 'search_jobs'
jobs = [
    {
        'id': 1,
        'title': 'Développeur web',
        'description': 'Développeur web expérimenté pour travailler sur des projets de grande envergure',
        'qualifications': ['Bac+3 en informatique', 'Maîtrise de PHP, JavaScript, HTML et CSS']
    },
    {
        'id': 2,
        'title': 'Analyste financier',
        'description': 'Recherche analyste financier expérimenté pour travailler dans une entreprise de renom',
        'qualifications': ['Bac+5 en finance', 'Expérience de 5 ans minimum dans un poste similaire']
    },
    {
        'id': 3,
        'title': 'Chef de projet',
        'description': 'Recherche chef de projet pour gérer des projets de grande envergure',
        'qualifications': ['Bac+5 en informatique', 'Expérience de 3 ans minimum en gestion de projets']
    }
]

user_input = 'web'

matching_jobs = search_jobs(jobs, user_input)



# Exemple de job à afficher
print(matching_jobs)
