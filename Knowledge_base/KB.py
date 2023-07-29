import pandas as pd
from pyswip import Prolog


def create_kb(dataset):
    experience_level = ['SE', 'MI', 'EN', 'EX']
    job_title = ['Data Engineer', 'Data Scientist', 'Data Analyst', 'Machine Learning Engineer', 'Analytics Engineer']
    salary_usd_range = [5132, 450000]
    employee_residence = ['US', 'GB', 'CA', 'ES', 'IN', 'Cl']
    company_location = ['US', 'GB', 'CA', 'ES', 'IN']
    company_size = ['S', 'M', 'L']
    cluster = [0, 1, 2]

    with open("KB.pl", "w") as file:

        # definizione degli assiomi della kb
        for el in experience_level:
            file.write(f'experience_level(\"{el}\").\n')

        for et in job_title:
            file.write(f'employment_type(\"{et}\").\n')

        file.write(f'salary_range({salary_usd_range[0]}, {salary_usd_range[1]}).\n')

        for er in employee_residence:
            file.write(f'employee_residence(\"{er}\").\n')

        for cl in company_location:
            file.write(f'company_location(\"{cl}\").\n')

        for cs in company_size:
            file.write(f'company_size(\"{cs}\").\n')

        for c in cluster:
            file.write(f'cluster({c}, "Cluster").\n')

        for index, row in dataset.iterrows():
            file.write(f'all_data(\"{row["experience_level"]}\", \"{row["job_title"]}\", {row["salary_in_usd"]}, '
                       f'\"{row["employee_residence"]}\", \"{row["company_location"]}\", \"{row["company_size"]}\", '
                       f'\"{row["cluster"]}\").\n')

        for index, row in dataset.iterrows():
            file.write(f'role(\"{row["job_title"]}\").\n')

        for index, row in dataset.iterrows():
            file.write(f'experience(\"{row["experience_level"]}\").\n')

        for index, row in dataset.iterrows():
            file.write(f'experience_and_salary(\"{row["experience_level"]}\", {row["salary_in_usd"]}).\n')

        for index, row in dataset.iterrows():
            file.write(f'experience_salary_and_location(\"{row["experience_level"]}\", {row["salary_in_usd"]}, \"{row["company_location"]}\").\n')

        for index, row in dataset.iterrows():
            file.write(f'role_salary_and_cluster(\"{row["job_title"]}\", {row["salary_in_usd"]}, \"{row["cluster"]}\").\n')


def create_rules():
    with open("KB.pl", "a") as file:

        # verifica se uno stipendio è alto
        file.write(f'''is_high_salary(Salary) :-
            Salary > 150000.''')

        # conta le occorrenze di un determinato lavoro
        # Role: ruolo svolto dal lavoratore
        # Count: tiene il conto delle occorrenze
        file.write(f'''\ncount_role_occurrences(Role, Count) :-
            findall(Role, role(Role), Roles),
            length(Roles, Count).''')

        # determina i ruoli più comuni
        # Role: ruolo svolto dal lavoratore
        file.write(f'''\ncommon_roles(Role) :-
            employment_type(Role),
            count_role_occurrences(Role, Count),
            Count >= 500.''')

        # determina il salario medio in base al livello di esperienza del lavoratore
        # ExperienceLevel: livello di esperienza del lavoratore all'interno dell'azienza
        # AverageSalary: salario medio
        file.write(f'''\naverage_salary_for_experience(ExperienceLevel, AverageSalary) :-
            experience(ExperienceLevel),
            findall(Salary, experience_and_salary(ExperienceLevel, Salary), Salaries),
            length(Salaries, Count),
            sum_list(Salaries, Total),
            AverageSalary is Total / Count.''')

        # stipendio medio in base al grado di esperienza del lavoratore e al paese in cui lavora
        # ExperienceLevel: livello di esperienza del lavoratore all'interno dell'azienza
        # CompanyLocation: luogo in cui è situata l'azienda
        # AverageSalary: salario medio
        file.write(f'''\naverage_salary_for_experience_country(ExperienceLevel, CompanyLocation, AverageSalary) :-
            findall(Salary, experience_salary_and_location(ExperienceLevel, Salary, CompanyLocation), Salaries),
            length(Salaries, Count),
            sum_list(Salaries, Total),
            AverageSalary is Total / Count.''')

        # stipendio medio in base al lavoro e al cluster
        # Role: ruolo svolto dal lavoratore
        # Cluster: categoria a cui appartiene il lavoratore
        # AverageSalary: salario medio
        file.write(f'''\naverage_salary_for_job_cluster(Role, Cluster, AverageSalary) :-
            findall(Salary, role_salary_and_cluster(Role, Salary, Cluster), Salaries),
            length(Salaries, Count),
            sum_list(Salaries, Total),
            AverageSalary is Total / Count.''')



def ask_queries():
    prolog = Prolog()
    prolog.consult('KB.pl')

    print(list(prolog.query('count_role_occurrences("Data Engineer", Count)')))
    print(list(prolog.query('count_role_occurrences("Data Scientist", Count)')))
    print(list(prolog.query('count_role_occurrences("Data Analyst", Count)')))
    print(list(prolog.query('count_role_occurrences("Machine Learning Engineer", Count)')))
    print(list(prolog.query('count_role_occurrences("Analytics Engineer", Count)')))

    result = list(prolog.query('average_salary_for_experience("EN", AverageSalary)'))
    print('\n', result[0])
    print(bool(list(prolog.query(f'is_high_salary({result[0]["AverageSalary"]})'))))

    result = list(prolog.query('average_salary_for_experience("MI", AverageSalary)'))
    print('\n', result[0])
    print(bool(list(prolog.query(f'is_high_salary({result[0]["AverageSalary"]})'))))

    result = list(prolog.query('average_salary_for_experience("SE", AverageSalary)'))
    print('\n', result[0])
    print(bool(list(prolog.query(f'is_high_salary({result[0]["AverageSalary"]})'))))

    result = list(prolog.query('average_salary_for_experience("EX", AverageSalary)'))
    print('\n', result[0])
    print(bool(list(prolog.query(f'is_high_salary({result[0]["AverageSalary"]})'))))

    print('')
    print(list(prolog.query('common_roles(Role)')))

    print('')
    print(list(prolog.query(f'average_salary_for_experience_country("EN", "US", AverageSalary)')))
    print(list(prolog.query(f'average_salary_for_experience_country("EN", "GB", AverageSalary)')))
    print(list(prolog.query(f'average_salary_for_experience_country("EN", "CA", AverageSalary)')))
    print(list(prolog.query(f'average_salary_for_experience_country("EN", "ES", AverageSalary)')))
    print(list(prolog.query(f'average_salary_for_experience_country("EN", "IN", AverageSalary)')))

    print('')
    print(list(prolog.query(f'average_salary_for_job_cluster("Data Engineer", "0", AverageSalary)')))
    print(list(prolog.query(f'average_salary_for_job_cluster("Data Engineer", "1", AverageSalary)')))
    print(list(prolog.query(f'average_salary_for_job_cluster("Data Engineer", "2", AverageSalary)')))

# MAIN
dataset = pd.read_csv('..\Datasets\ds_salaries_usd+clusters.csv')
create_kb(dataset)
create_rules()
ask_queries()
