def generate_reports(title, *args, **kwargs):
    if "skip_section" in kwargs.keys():
        skip_section = kwargs["skip_section"]
    else:
        skip_section = []
    section = [i for i in args if args.index(i)+1 not in skip_section]
    formatted_list = [f"\tsection {section.index(elem)+1}: {elem}" for elem in section]
    section = '\n'.join(formatted_list)
    with open("file.txt", 'w') as file:
        file.write(f'''
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