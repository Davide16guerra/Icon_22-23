import beliefNetwork


def help():
    print("discrete attributes available: \n\n"
          "- experience_level --> [SE, MI, EN, EX]\n"
          "- job_title --> [Principal Data Scientist, ML Engineer, Data Scientist, Applied Scientist, \n\t"
          "Data Analyst, Data Modeler, Research Engineer, Analytics Engineer, Business Intelligence Engineer, Machine Learning Engineer, \n\t"
          "Data Strategist, Data Engineer, Computer Vision Engineer, Data Quality Analyst, Compliance Data Analyst, Data Architect, \n\t"
          "Applied Machine Learning Engineer, AI Developer, Research Scientist, Data Analytics Manager, Business Data Analyst, \n\t"
          "Applied Data Scientist, Staff Data Analyst, ETL Engineer, Data DevOps Engineer, Head of Data, Data Science Manager, \n\t"
          "Data Manager, Machine Learning Researcher, Big Data Engineer, Data Specialist, Lead Data Analyst, BI Data Engineer, \n\t"
          "Director of Data Science, Machine Learning Scientist, MLOps Engineer, AI Scientist, Autonomous Vehicle Technician, \n\t"
          "Applied Machine Learning Scientist, Lead Data Scientist,	Cloud Database Engineer, Financial Data Analyst, Data Infrastructure Engineer, \n\t"
          "Software Data Engineer, AI Programmer, Data Operations Engineer, BI Developer, Data Science Lead, Deep Learning Researcher, \n\t"
          "BI Analyst, Data Science Consultant,	Data Analytics Specialist, Machine Learning Infrastructure Engineer, BI Data Analyst, \n\t"
          "Head of Data Science, Insight Analyst, Deep Learning Engineer, Machine Learning Software Engineer, Big Data Architect, \n\t"
          "Product Data Analyst, Computer Vision Software Engineer, Azure Data Engineer, Marketing Data Engineer, Data Analytics Lead, \n\t"
          "Data Lead, Data Science Engineer, Machine Learning Research Engineer, NLP Engineer, Manager Data Management, Machine Learning Developer, \n\t"
          "3D Computer Vision Researcher, Principal Machine Learning Engineer, Data Analytics Engineer, Data Analytics Consultant, Data Management Specialist, \n\t"
          "Data Science Tech Lead, Data Scientist Lead, Cloud Data Engineer, Data Operations Analyst, Marketing Data Analyst, Power BI Developer, \n\t"
          "Product Data Scientist, Principal Data Architect, Machine Learning Manager, Lead Machine Learning Engineer, ETL Developer, \n\t"
          "Cloud Data Architect, Lead Data Engineer, Head of Machine Learning, Principal Data Analyst, Principal Data Engineer, \n\t"
          "Staff Data Scientist, Finance Data Analyst]\n"
          "- salary_in_usd --> [-36708, 36708-38703.5, 38703.5-62863, 62863-63020, 63020-100250, 100250-165110, +165110]\n"
          "- employee_residence --> [US, GB, CA, ES, IN, Cl]\n"
          "- company_location --> [US, GB, CA, ES, IN]\n"
          "- company_size --> [S, M, L]\n"
          "- cluster --> [0, 1, 2]\n")

    print("Ex. quary --> salary_in_usd:  experience_level=SE, job_title=Data Analyst\n")

    print("for exit write --> exit\n")


print("max number of parents (1,2,3):")
while 1 != 0:
    try:
        maxNofParents = input(">> ")
        bn = beliefNetwork.BeliefNetwork(int(maxNofParents))
        break
    except Exception:
        print('invalid command!')

print("\nfor info write --> help\n")

while 1 != 0:
    str = input(">> ")

    if str == 'help':
        help()

    elif str == 'exit':
        exit(0)

    else:
        try:
            bn.ask_queries(str)
        except Exception:
            print('invalid command!')