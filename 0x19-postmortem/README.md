# My first postmortem
# Postmortem: June 19, 2024 Outage

## Issue Summary

**Duration of Outage**:
- **Start**: June 19, 2024, 14:00 WAT
- **End**: June 19, 2024, 15:00 WAT

**Impact**:
- The banking web application was down, preventing all users from accessing their accounts, performing transactions, or creating new accounts.
- Approximately 100% of users were affected.

**Root Cause**:
- The outage was caused by a missing PHP module required by the Apache server to serve the web application correctly.

## Timeline

- **14:00 WAT**: Issue detected via a monitoring alert indicating that the Apache server was returning HTTP 500 errors.
- **14:05 WAT**: The on-call engineer received the alert and began investigating the Apache server logs.
- **14:10 WAT**: Initial hypothesis was a configuration error in the Apache server or a corrupted PHP file.
- **14:20 WAT**: Misleading path: Engineer checked the Apache configuration files and restarted the Apache service, but the issue persisted.
- **14:30 WAT**: The issue was escalated to the web development team for further analysis.
- **14:40 WAT**: Upon reviewing the error logs, the team identified that the error was related to a missing PHP module that the application depended on.
- **14:50 WAT**: The required PHP module was installed, and the Apache server was restarted.
- **15:00 WAT**: Issue resolved, and the application was fully operational again. Monitoring confirmed that the HTTP 500 errors were no longer occurring.

## Root Cause and Resolution

**Root Cause**:
- The root cause was a missing PHP module (`php-missing-module`) that the Apache server required to run the banking web application. This module was not installed on the server, leading to HTTP 500 Internal Server Error responses when users tried to access the site.

**Resolution**:
- The missing PHP module was installed using the package manager. The Apache service was then restarted to apply the changes. Once the module was in place, the web application began functioning correctly again.

## Corrective and Preventative Measures

### Improvements/Fixes

1. **Enhanced Monitoring**: Implement more detailed monitoring for specific application dependencies to catch missing modules or packages before they cause outages.
2. **Automated Configuration Management**: Use a configuration management tool to ensure that all required packages are installed on the server.
3. **Regular Audits**: Conduct regular audits of server configurations and dependencies to ensure all necessary components are present.

### Task List

1. **Patch Nginx/Apache Server**: Ensure all required PHP modules are installed and up-to-date.
2. **Add Dependency Monitoring**: Set up monitoring to alert when critical packages are missing or become corrupted.
3. **Implement Puppet Configuration**:
   ```puppet
   package { 'php-missing-module':
     ensure => installed,
   }

   service { 'apache2':
     ensure    => running,
     enable    => true,
     subscribe => Package['php-missing-module'],
   }
#### [URL FOR THE TASK](https://docs.google.com/document/d/1PqEJypEnsQxncfOBrteigxvsInBihDDgW7_OBV71WNY/edit?usp=sharing)








# Make people want to read your postmortem

# 🚨 Postmortem: The Great Banking Web Application Outage of 2024 🚨


## Issue Summary

**Duration of Outage**:
- **Start**: June 19, 2024, 14:00 WAT
- **End**: June 19, 2024, 15:00 WAT

**Impact**:
- The banking web application was down, preventing all users from accessing their accounts, performing transactions, or creating new accounts. 🏦💥
- Approximately 100% of users were affected. Yes, ALL of them. 😱

**Root Cause**:
- The culprit? A missing PHP module that the Apache server needed to run our beloved web application. PHP, why do you do this to us? 😓

## Timeline

- **14:00 WAT**: Issue detected via a monitoring alert indicating that the Apache server was returning HTTP 500 errors. (Cue the ominous music) 🎵
- **14:05 WAT**: The on-call engineer received the alert and began investigating the Apache server logs. 🔍
- **14:10 WAT**: Initial hypothesis was a configuration error in the Apache server or a corrupted PHP file. 🧐
- **14:20 WAT**: Misleading path: Engineer checked the Apache configuration files and restarted the Apache service, but the issue persisted. 🤔
- **14:30 WAT**: The issue was escalated to the web development team for further analysis. Team assemble! 🦸‍♂️🦸‍♀️
- **14:40 WAT**: Upon reviewing the error logs, the team identified that the error was related to a missing PHP module that the application depended on. Eureka! 🕵️‍♀️
- **14:50 WAT**: The required PHP module was installed, and the Apache server was restarted. ✨
- **15:00 WAT**: Issue resolved, and the application was fully operational again. Monitoring confirmed that the HTTP 500 errors were no longer occurring. High fives all around! 🙌

## Root Cause and Resolution

**Root Cause**:
- The root cause was a missing PHP module (`php-missing-module`) that the Apache server required to run the banking web application. This module was not installed on the server, leading to HTTP 500 Internal Server Error responses when users tried to access the site. It’s like trying to bake a cake without flour. 🍰❌

**Resolution**:
- The missing PHP module was installed using the package manager. The Apache service was then restarted to apply the changes. Once the module was in place, the web application began functioning correctly again. Back to business as usual! 💼

## Corrective and Preventative Measures

### Improvements/Fixes

1. **Enhanced Monitoring**: Implement more detailed monitoring for specific application dependencies to catch missing modules or packages before they cause outages. Like having a smoke detector in your kitchen. 🚨
2. **Automated Configuration Management**: Use a [configuration management tool](https://puppet.com/docs/puppet/latest/puppet_index.html) to ensure that all required packages are installed on the server. Think of it as having a personal assistant who never forgets. 🤖
3. **Regular Audits**: Conduct regular audits of server configurations and dependencies to ensure all necessary components are present. It’s like spring cleaning but for your servers. 🧹

### Task List

1. **Patch Nginx/Apache Server**: Ensure all required PHP modules are installed and up-to-date. 🛠️
2. **Add Dependency Monitoring**: Set up monitoring to alert when critical packages are missing or become corrupted. 🕵️‍♂️
3. **Implement Puppet Configuration**:
   ```puppet
   package { 'php-missing-module':
     ensure => installed,
   }

   service { 'apache2':
     ensure    => running,
     enable    => true,
     subscribe => Package['php-missing-module'],
   }

#### [URL FOR THE TASK](https://docs.google.com/document/d/1nuF40ETvj7TR4E1a9BcshbI8d_ISQnUzVg4k4MeXJYI/edit?usp=sharing)
