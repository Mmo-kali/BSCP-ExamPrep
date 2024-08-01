IMPORTANT: [https://github.com/ChrisM-X/PortSwigger-Academy-CheatSheets/tree/master/SQL Injection#examples](https://github.com/ChrisM-X/PortSwigger-Academy-CheatSheets/tree/master/SQL%20Injection#examples)

---

---

**SQL INJECTION CHEAT SHEET:** https://portswigger.net/web-security/sql-injection/cheat-sheet

# How to detect SQL injection Vulnerabilities?

**How do we detect SQLi on a Web application?** 

- SQL injection vulnerabilities can  be detected in a manual systematic set of tests.
- Or **Automated with SQL-Map**

### **Where do we check or Test for these vulnerabilities?**

- To test for SQLi vulnerabilities we should test against every entry point to the application.
    
    
    **What is an Entry Point?** 
    
    - An entry point to an application is any place where attacker-controllable data can enter the application’s processing.
        - This includes parameters or other data within the URL query string and message body, the URL file path, and HTTP request headers.

---

### **How do we test for SQLi vulnerability / what input do we give?**

- to test for a SQLi vulnerability the typical input would be different based off of the type of information we are trying to get.

**Looking for errors or other anomalies?** 

- Submit a single/double quote characters and look for errors or anomalies:
    - '
    - ''
    - '--
    - '#

**Looking for systematic differences in the application responses?** 

- Some SQL-specific syntax that evaluates to the base (original) value of the entry point, and to a different value

**Differences in application responses?** 

- Boolean conditions such as `OR 1=1` and `OR 1=2`, and look for differences in the application's responses.

> *The described steps typically identify most SQL injection vulnerabilities, even when no results or error information are sent back to the browser. However, for some cases, advanced techniques like time delays may be required to confirm a vulnerability. — [From web app hacker handbook page 323]*
>
