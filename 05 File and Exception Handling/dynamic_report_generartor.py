#Assignment Dynamic Report Generator
def generate_report(Title,Section1,Section2,Section3, author, date, conclusion, skip_section):
    print("Report Title : ", Title)
    print("="*50)
    print("Author : ", author)
    print("Date : ", date)
    print()
    print("Report Sections : ")
    print("-"*50)
    if 1 not in skip_section:
        print("Section 1 : ", Section1)
    if 2 not in skip_section:
        print("Section 2 : ", Section2)
    if 3 not in skip_section:
        print("Section 3 : ", Section3)
    print("Conclusion : ")
    print("-"*50)
    print("Conclusion : ", conclusion)



generate_report("Montly Sales Report","Introduction: Overview of sales performance",
                "Data Analytics : Breakdown sales data by region","Market Trends: Analysis of current market trends"
                ,author = "John Doe", date = "September 2024", conclusion = "Overall, sales have increased by 15% compared to the previous month. ",
                skip_section =[2])



# output
# Report Title :  Montly Sales Report
# ==================================================
# Author :  John Doe
# Date :  September 2024

# Report Sections : 
# --------------------------------------------------
# Section 1 :  Introduction: Overview of sales performance
# Section 3 :  Market Trends: Analysis of current market trends
# Conclusion : 
# --------------------------------------------------
# Conclusion :  Overall, sales have increased by 15% compared to the previous month.




#----------------------------------------------------------------

# Another way to do that by using args and kwargs
def generate_reports(title, *args, **kwargs):
    if "skip_section" in kwargs.keys():
        skip_section = kwargs["skip_section"]
    else:
        skip_section = []
    section = [i for i in args if args.index(i)+1 not in skip_section]
    formatted_list = [f"\tsection {section.index(elem)+1}: {elem}" for elem in section]
    section = '\n'.join(formatted_list)
    print(f'''
    Report Title : {title}
    {"="*50}
    Author : {kwargs['author']}
    Date   : {kwargs['date']}

    Report Sections :
    {"-"*50}
{section}

    Conclusion :
    {"-"*50}
    Conclusion : {kwargs['conclusion']}''')

generate_reports("Montly Sales Report","Introduction: Overview of sales performance",
                "Data Analytics : Breakdown sales data by region","Market Trends: Analysis of current market trends"
                ,author = "John Doe", date = "September 2024", conclusion = "Overall, sales have increased by 15% compared to the previous month. ",
                skip_section =[2])



# output

#     Report Title : Montly Sales Report
#     ==================================================
#     Author : John Doe
#     Date   : September 2024
          
#     Report Sections : 
#     --------------------------------------------------
# 	section 1: Introduction: Overview of sales performance
# 	section 2: Market Trends: Analysis of current market trends     

#     Conclusion :
#     --------------------------------------------------
#     Conclusion : Overall, sales have increased by 15% compared to the previous month. 