# Behave Demo

Repository with demo code prepared for [behave workshop](https://aga-ma.github.io/behave_workshop/#/)

- [Behave demo](#behave-demo)  
- [Feature files](#feature-files)
- [Step definitions](#step-definitions)

# Feature Files

Feature files has a natural language format - describing a feature or part of a feature with representative examples of
expected outcomes

Given, when, then (and, but) - forms the actual steps. Those map to python step implementation.

<span style="color: red;">**Feature**</span>: feature name  

&nbsp;&nbsp;<span style="color: blue;">**Scenario**</span>: some scenario   
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: green;">**Given**</span> some condition <span style="color: grey;">#put the system in a known state</span>   
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: green;">**When**</span> some action taken <span style="color: grey;">#we take key action the user or external system performs</span>   
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: green;">**Then**</span> some result is expected. <span style="color: grey;">#we observe outcomes</span>   


You may also include "And" or "But" as a step - those are renamed by behave to take the name of their preceding step  

# Step definitions

Steps used in the scenarios are implemented in Python files in the `steps` directory.
You call the files whatever you like as long as they use the `.py` extension. You don't need to tell behave which ones to
use - it will use all of them.

Step definition - a python function decorated by a matching string in a step definition module.  
Given, When, Then steps are "glued" to a step definitions with decorators.  

Steps are identified using decorators which match the predicate from the feature file: given, when, then, step.  
The decorators accepts a string containing the rest of the phrase used in the scenario step.  

The function names do not need to have a unique symbol name. The text matching selects the step function from the step 
registry before it is called as anonymous function.  