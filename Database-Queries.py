
from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.sql_database import SQLDatabase
from langchain.llms.openai import OpenAI
from langchain.agents import AgentExecutor
from langchain import OpenAI, SQLDatabase, SQLDatabaseChain
from IPython.display import Markdown, HTML


username  = 'nlp'                  # change it to a valid user on your db
password  = 'password'  # fill in the appropriate password
uri       = f"mysql+pymysql://{username}:{password}@localhost/foodmart"

db = SQLDatabase.from_uri(uri)
toolkit = SQLDatabaseToolkit(db=db)

agent = create_sql_agent(
    llm=OpenAI(temperature=0),
    toolkit=toolkit,
    verbose=True
)

"""## Querying the database with nlp

### How many employees are there?
"""

query = 'How many employees are there?. Show also the sql query used to find this.'

agent.run(query)

"""### Min, max and average salary of the employees?"""

query = 'Retrieve all the minimum, maximum, and the average salary.'
agent_executor.run(query)

"""### The highest earners"""

query = """Return the full name and salary for each of the top 20 different highest earning employees.
Show each row of the result in this format:

<tr><td>[employee full name] </td><td>[salary]</td></tr>

"""

result = agent_executor.run(query)
display(HTML("<table> " + result + "</table>"))

"""### Who specifically is the highest paid?"""

query = """
Who earned the highest salary, and how much did the employee earn?.
For this employee, find the full name, title, gender, and education level. Return the answer in this format:

> **Query used** [query]
>
> **Employee name** [employee], of gender [gender] and education level [education level] with title [title]
>
> ** Salary** [salary]

"""
result = agent_executor.run(query)
display (Markdown(result))

"""### Stores and their total sales."""

query = """
Consider all the stores. For each store, return the name of the store, the state it belongs to, and the total store sales for that store.
Return the results in the following format, for each store:

<tr><td>[store name] </td><td>[state]</td><td>[total store sales]</td></tr>
"""


result = agent.run(query)

html = f"""
<table>
<tr><td><b>STORE NAME</b> </td><td> <b>STATE</b></td><td><b>TOTAL SALE </b></td></tr>

{result}
</table>
"""

display(HTML(html))

"""## Sequential Chains

Find the median total sales for the stores.

We know that mysql database does not directly support the `median()` function. So let us use the math tool to compute the median sales, after we have retrieved the total sales for the stores.
"""

from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chains import SimpleSequentialChain
from langchain import OpenAI, LLMMathChain

llm = OpenAI(temperature=0)
llm_math = llm_math = LLMMathChain(llm=llm, verbose=True)



overall_chain = SimpleSequentialChain(chains=[agent, llm_math], verbose=True)

query = """
Fetch the total sales of each of the stores as a sorted list of amounts,
then use math to compute the median
"""
overall_chain.run (query)

