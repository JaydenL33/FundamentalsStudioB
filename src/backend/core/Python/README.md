# Libs and Dependency Management
* Semantically, all utilities fall into some category of functionality. 
* Each is appended to their corresponding category of semantic lib file.
* This maintains dependencies seperately from "business" code (source app code), avoiding circular dependency issues.
* Semeantically, it may make sense to add a category of util's that depends on another, this is fine! It simply lives in its own 
namespace/module
