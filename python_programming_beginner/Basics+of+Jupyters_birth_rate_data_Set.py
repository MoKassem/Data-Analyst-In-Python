
# coding: utf-8

# <p>In this notebook, I'm exploring a dataset on births in the U.S compiled by <strong>FiveThirtyEigh</strong>.</p>
# 
# 
# <h4>The dataset contains the following columns:</h4>
# <ul>
#     <li>year: Year (1994 to 2003).</li>
#     <li>month: Month (1 to 12).</li>
#     <li>date_of_month: Day number of the month (1 to 31).</li>
#     <li>day_of_week: Day of week (1 to 7).</li>
#     <li>births: Number of births that day.</li>
# </ul>
# 
# 
# <p>The dataset can be found here: <a href="https://raw.githubusercontent.com/fivethirtyeight/data/master/births/US_births_1994-2003_CDC_NCHS.csv">dataset</a>
# 

# In[1]:


def read_csv(file_name):
    final_list=[]
    file = open (file_name, "r")
    string_list = file.read().split("\n")
    string_list =  string_list[1:]
   
    for string in string_list:
        int_fields= []
        string_fields = string.split(',')
        for field in string_fields:
            int_fields.append(int(field))
        final_list.append (int_fields)
    return final_list
            


# In[2]:


cdc_list = read_csv ("US_births_1994-2003_CDC_NCHS.csv")
cdc_list [:10]


# Function <strong>month_births(): </strong> takes a single, required argument (a list of lists) and returns a dictionary containing the total number of births for each unique value of the <i>day_of_month</i> column.

# In[3]:


def month_births (cdc_month_births_list):
    births_per_month = {}
    for birth_list in cdc_month_births_list:
        month = birth_list [2]
        birth =  birth_list [4]
        if month in births_per_month:
            births_per_month[month]+=birth
        else:
            births_per_month[month]= birth
    return births_per_month
        
    


# In[4]:


cdc_month_births = month_births(cdc_list)
cdc_month_births


# Function <strong>dow_births(): </strong> takes a single, required argument (a list of lists) and returns a dictionary containing the total number of births for each unique value of the <i>day_of_week</i> column.

# In[5]:


def dow_births (cdc_month_births_list):
    births_per_week_day = {}
    for birth_list in cdc_month_births_list:
        day_of_week = birth_list [3]
        birth =  birth_list [4]
        if day_of_week in births_per_week_day:
            births_per_week_day[day_of_week]+=birth
        else:
            births_per_week_day[day_of_week] = birth
    return births_per_week_day


# In[6]:


cdc_day_births = dow_births(cdc_list)
cdc_day_births


# In[7]:


def calc_counts(data_list, index_to_sum_over):
    total_birth_per_index = {}
    for d_list in data_list:
        index_value = d_list [index_to_sum_over]
        birth_at_index_val = d_list [len(d_list) - 1] 
        if index_value in total_birth_per_index:
            total_birth_per_index[index_value]+=birth_at_index_val
        else: 
            total_birth_per_index[index_value]=birth_at_index_val
    return total_birth_per_index


# In[8]:


cdc_year_births = calc_counts (cdc_list, 0)
cdc_year_births


# In[9]:


cdc_month_births = calc_counts (cdc_list, 1)
cdc_month_births


# In[10]:


cdc_dom_births = calc_counts (cdc_list, 2)
cdc_dom_births


# In[11]:


cdc_dow_births = calc_counts (cdc_list, 3)
cdc_dow_births


# <p>A function that can calculate the <strong>min</strong> and <strong>max</strong> values for any dictionary that's passed in.</p>

# In[22]:


def min_max_dict(dictionary):
    dict_list = list(dictionary.values())
    min =  dict_list[0]
    max = min
    for el in dict_list:
        if el < min:
            min=el
        else:
            max=el
    return [min, max]


# In[24]:


test_dict ={
    "1": 2,
    "2": 40,
    "3": 16,
    "4": 8
}
min_max_list = min_max_dict (test_dict)
min_max_list


# In[48]:


def calc_day_of_week_births_per_year(data_list, year, day_of_week, index_day_of_week):
    sum=0
    for d_list in data_list:        
        d_year = d_list[0]
        d_day_of_week = d_list[index_day_of_week]
        birth = d_list [len(d_list) - 1]
        if d_year == year and d_day_of_week == day_of_week:
                sum=+birth
    return sum
            
    


# In[54]:


def get_day_of_week_births_per_year (data_list, start_year, end_year, day_of_week, index_day_of_week):
    my_dictionat = {}
    for year in list(range(start_year, end_year)):
        my_dictionat [year] = calc_day_of_week_births_per_year (data_list, year, day_of_week, index_day_of_week)
    return my_dictionat


# In[55]:


saturday_birth_per_year = get_day_of_week_births_per_year (cdc_list, 1994, 2003, 7, 3)
saturday_birth_per_year

