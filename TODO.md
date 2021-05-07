https://github.com/jdavisclark/CaseConversion/issues/

* multi-line support: 
	* change individual lines when selection includes multiple lines
	* change whole file
* new cases
	* uppercase
	* lowercase
* preserve separators before, during, and after
	* __my_var__
	* __my_var
	* my_var__
	* my__var
	* php variable prefix $
	* file extensions    Admin/SomeModule/UsedClass.php
* keep changed text highlighted
* support more characters
	* unicode
	* escaped characters


* Handle Inconsistent captialization
	* Converting MyNAME to split words becomes My N A M E instead of My NAME

* add case conversion context menu
* be able to set the cases toggle_case will cycle through




# Inconsistent camelCase
https://github.com/jdavisclark/CaseConversion/issues/45
```
HTML tag
SCRIPT tag
```
becomes
```
htmlTag
sCRIPTTag
```