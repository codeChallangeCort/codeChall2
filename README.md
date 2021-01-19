# codeChall2
#### Code Challange

###### Challange 

Users of the Corteva website can provide their name and email address in order to register for a free newsletter written by Corteva agronomists on Pioneer seed products. 

Corteva wants to share the list of newsletter subscribers across multiple parts of the business using their centralized data warehouse. 

Data must be loaded to the data warehouse via a RESTful API using a JSON format. 

The problem is to convert 1 or more CSV-formatted files containing the exported list of new subscribers into JSON format for import into the data warehouse. 

The output of the command-line driven application should be a single file containing a list of JSON objects. 

A very basic JSON format for the output has been proposed by the data warehouse team and they have provided an example named user_list_ex.json and a schema description in user_list_schema.json. You may use this schema for your json output or you may modify it. If your application uses a modified schema, please provide a new schema description file to describe your schema.

This application must be written using a modern, flexible scripting language such as Python, Ruby, or Perl. A sample input file named pipeline_input_user_export-vx.csv is included with this problem statement.


###### n1.csv and n2.csv are the sample input files in the folder for testing purpose.

```
python start.py filename.csv filename.csv
```

