# Red Rover Code Puzzle

Thank you for your interest in joining our team.  The following coding exercise helps us get a sense for your approach to turning a requirement into code. If you have any questions please reach out.

## How to Run App

* Ensure that Python is installed, with a minimum version of 3.7.
* In your terminal of choice, navigate to the directory which contains this source code.
* Run the following command to execute the program:
  * `python main.py`

## Instructions

Using any technology of your choice, convert the following string: 

`"(id, name, email, type(id, name, customFields(c1, c2, c3)), externalId)"`

To this output:

```cmd
- id
- name
- email
- type
  - id
  - name
  - customFields
    - c1
    - c2
    - c3
- externalId
```

And also to this output:

```cmd
- email
- externalId
- id
- name
- type
  - customFields
    - c1
    - c2
    - c3
  - id
  - name
```

Please send access to the source and a runnable copy of your app. 
