# Certified Docusign IAM Integration & Extension Developer

Cleaned study material from the self-paced courses in the certification learning paths.

## Official Exam Overview (Prep Guide v. 2026)

- 60 multiple-choice items. **Some questions have more than one correct answer.** Answer every question; there is no penalty for guessing.
- 150 minutes, proctored online via Certiverse (Safe Exam Browser, webcam, government photo ID).
- Passing score: 70%. Retake waiting period: 45 days.

| Section | Weight |
|---|---|
| 1. API Authentication | 13% |
| 2. Go Live Process | 11% |
| 3. Docusign Connect | 12% |
| 4. eSignature API | 16% |
| 5. eSignature Features & Web Forms | 11% |
| 6. Agreement Manager API | 6% |
| 7. Workflow Builder & Workflow API | 15% |
| 8. App Center & Extension Apps | 16% |

Out of scope (removed from these notes): Responsive Signing, PowerForms, Workspaces API, and the Agreement Manager UI-only topics (sharing permissions, dashboards/reports/renewals). No official exam objective covers them.

## Get Started with Docusign for Developers

### Docusign for Developers Overview 30 min

Docusign for Developers Overview
Introduction to Docusign for Developers
AGREEMENT APIS
Integrate Signing with the eSignature API
Integrate Agreement Data with the Agreement Manager API
Integrate Workflows with the Workflow Builder API
Integrate More Features with Additional Agreement APIs
WORKFLOWS
Create Workflows
EXTENSION APPS
Integrate External Features with Extension Apps
Scenario: Plan Docusign Integrations
Introduction to Docusign for Developers
Integrate data from the entire agreement lifecycle into your business systems, and extend the IAM platform with external features.
Docusign for Developers is a set of tools to support developers integrating Docusign services into custom applications. The platform also provides tools for developers extending Docusign products using third-party services.
Docusign for Developers includes APIs, the Workflow Builder, Extension Apps, and the Developer Console.
APIs
Docusign offers a collection of APIs to support creating, committing to, and managing agreements.
eSignature API
Agreement Manager API
Workflow Builder API
Web Forms API
Connected Fields API
ID Evidence API
Workflow Builder
Workflow Builder is a low-code tool for building agreement workflows to automate your organization's agreement processes and give you insight into those agreements.
Workflows are highly customizable to support a wide variety of agreement processes that involve multiple steps, parties, and Docusign features.
Extension Apps and Developer Console
Extension apps enable you to build solutions that connect third-party services into Docusign. They enable you to include additional functionality, such as:
Archiving documents in an external application.
Verifying data such as a user's bank account, US Social Security Number, and postal and email address.
Reading and writing data back into another application.
After you build an extension app, you can publish it to the Docusign App Center
Extension apps can be public, enabling customers to discover and install them to extend and enhance their agreement processes. You can also create private extension apps that are available only within your organization.
You can leverage the self-serve Docusign Developer Console to build your own extension app and publish it to the Docusign App Center. Customers can then install your application to enhance their agreement processes with your service.
The Docusign App Center can be accessed via the following URLs:
Production: apps.docusign.com/app-center
Demo: apps-d.docusign.com/app-center
Lesson 2 - Integrate Signing with the eSignature API

Docusign for Developers Overview
Welcome to the Docusign for Developers Overview self-paced course. After reviewing this course, you will be able to:
Explain the features available in Docusign for Developers.
Describe common use cases for building custom integrations using the eSignature API, Agreement Manager API, Workflow Builder and API, Web Forms API, Connected Fields API, and the ID Evidence API.
Describe common use cases for integrating a service into Docusign through an extension app, and explain the process of creating one.
Identify resources to help you integrate with and extend the Docusign platform.
Introduction to Docusign for Developers
AGREEMENT APIS
Integrate Signing with the eSignature API
Integrate Agreement Data with the Agreement Manager API
Integrate Workflows with the Workflow Builder API
Integrate More Features with Additional Agreement APIs
WORKFLOWS
Create Workflows
EXTENSION APPS
Integrate External Features with Extension Apps
Scenario: Plan Docusign Integrations

Docusign for Developers Overview
Introduction to Docusign for Developers
AGREEMENT APIS
Integrate Signing with the eSignature API
Integrate Agreement Data with the Agreement Manager API
Integrate Workflows with the Workflow Builder API
Integrate More Features with Additional Agreement APIs
WORKFLOWS
Create Workflows
EXTENSION APPS
Integrate External Features with Extension Apps
Scenario: Plan Docusign Integrations
Lesson 5 - Integrate More Features with Additional Agreement APIs
Create Workflows
Objective: After reviewing this topic, you will be able to describe common use cases and resources for creating a workflow.
Note: workflows are available in all developer accounts, but only in certain production account plants. Contact Docusign Support
or your account team to find out whether workflows are available for your production account plan.
Workflow Builder
With Workflow Builder you can create workflows to automate business processes. Workflows offer basic conditionality, and support modules including ID Verification, Web Forms, Sign, and CLM, as well as partner applications from a variety of third-party services like ServiceNow, Stripe, and Google Drive.
Workflow Builder enables you to monitor workflows for visibility into user data, where they are in the process, and where they may be dropping off.
Business Use Cases
Property Sale
New Customer Intake
Workflows Development Process Overview
To build a workflow, you follow these steps in Workflow Builder:
1
Specify participants and any starting variables.
2
Add a step from the available options, then configure options for your step.
3
Continue to add steps until your workflow is complete.
4
Provide a name for your workflow, resolve any variable errors, then publish your workflow.
To learn how to create workflows, click the link for your account type, then register for the Docusign University course Build Agreement Workflows with Docusign (Customer
| Developer/Demo
| Employee
| Partner
)
Note: The Docusign Template Library offers pre-configured workflow samples to help you start building your own workflows.
| Developer/Demo
| Employee
| Partner
Lesson 7 - Integrate External Features with Extension Apps

Docusign for Developers Overview
Introduction to Docusign for Developers
AGREEMENT APIS
Integrate Signing with the eSignature API
Integrate Agreement Data with the Agreement Manager API
Integrate Workflows with the Workflow Builder API
Integrate More Features with Additional Agreement APIs
WORKFLOWS
Create Workflows
EXTENSION APPS
Integrate External Features with Extension Apps
Scenario: Plan Docusign Integrations
Lesson 4 - Integrate Workflows with the Workflow Builder API
Integrate More Features with Additional Agreement APIs
Objective: After reviewing this topic, you will be able to identify additional Docusign agreement APIs and describe use cases each one supports for custom integrations.
In addition to the eSignature API, Agreement Manager API, and Workflow Builder API, Docusign offers agreement APIs for a number of other features, including the following:
Web Forms API: Create, manage, and embed Docusign Web Forms.
Connected Fields API: Integrate data verification into Docusign agreements or workflows.
ID Evidence API: Retrieve evidence from a Docusign ID Verification event.
Note: The agreement APIs listed are available in all developer accounts, but only in certain production account plans. Contact Docusign Support
or your account team to find out whether these APIs are available for your production account plan.
Web Forms API
Docusign Web Forms enables you to build web pages that contain fields in which users enter data. User-entered form values can be dynamically incorporated into eSignature envelopes that users sign, as well as exported to your business applications. With the Web Forms builder, you can easily create a sequence of form pages, add form fields, set validation rules, and apply conditional logic.
Web Forms API
The Web Forms API enables you to create and integrate the web form instances that users fill out. You can also use the API to retrieve data about the web form configurations that are available in your Docusign account.
In addition to the Web Forms API, Docusign provides a JavaScript client SDK, Docusign JS, that you can use to seamlessly embed a web form instance into your website.
Business Use Cases
Financial Aid Application
Insurance Claims
Connected Fields API
Docusign data verification enables you to verify signer-provided information in real time with trusted databases. Implementing data verification avoids the need to correct data later, reducing costs and accelerating your agreement processes.
You can use Basic or Premium data verification to verify several common types of data using sources integrated with Docusign. You can also implement Custom data verification to securely verify data against internal systems or other authoritative data sources that you choose.
Connected Fields API
When you implement data verification in your custom apps, you can use the Connected Fields API to get information on the connected fields that your agreements use. The API provides the data model for each extension app that supports data verification or connected fields. Your integration can then use the data model to add the fields to your agreements and present them for signature.
ID Evidence API
Docusign ID Verification solutions enable you to authenticate and verify recipients' identities before they can review and sign their documents or as they complete workflow steps.
Docusign offers different variations of Docusign ID Verification to align with your specific needs. Different ID Verification configurations offer different verification methods.
For example, with the standard Docusign ID Verification configuration, recipients must identify themselves by providing an image of a valid government-issued photo ID, using an electronic or bank ID, using a CLEAR account (US residents only), or by going through knowledge-based authentication (US residents only).
ID Evidence API
Your account administrator can choose to configure your Docusign account to retain one or more types of ID Verification data. You can then use the ID Evidence API to retrieve the selected information about an ID verification event after an agreement participant successfully completes ID verification. For instance, for photo IDs your administrator can choose to make ID images available, as well as personal information and document details.
What Tools Are Available for Docusign Agreement API Developers?
→ Docusign provides several free tools and resources to help developers build integrations using Docusign Agreement APIs more efficiently, including SDKs and Quickstart.
SDKs
Docusign SDKs wrap Agreement APIs with objects, properties, and methods in your favorite programming language. SDKs are available for development in C#, Java, Node.js, PHP, Python, and Ruby.
SDKS
Quickstart
Docusign Quickstart is a free tool from Docusign that generates a code project, in your choice of Bash, C#, Java, Node.js, PHP, Python, PowerShell or Ruby, that is preconfigured with all the personalized developer account and OAuth implementation settings that you need to get started developing Docusign integrations.
QUICKSTART TOOL
Sample Apps
Try out sample apps that demonstrate common agreement API workflows and showcase best practices around implementation.
Other Tools
The Docusign Developer Center also offers additional tools and resources including an API explorer, a Postman collection, an OpenAPI specification, and IDE extensions for both Visual Studio Code and Visual Studio.
TOOLS OVERVIEW
Lesson 6 - Create Workflows

Docusign for Developers Overview
Introduction to Docusign for Developers
AGREEMENT APIS
Integrate Signing with the eSignature API
Integrate Agreement Data with the Agreement Manager API
Integrate Workflows with the Workflow Builder API
Integrate More Features with Additional Agreement APIs
WORKFLOWS
Create Workflows
EXTENSION APPS
Integrate External Features with Extension Apps
Scenario: Plan Docusign Integrations
Lesson 4 - Integrate Workflows with the Workflow Builder API
Integrate More Features with Additional Agreement APIs
Objective: After reviewing this topic, you will be able to identify additional Docusign agreement APIs and describe use cases each one supports for custom integrations.
In addition to the eSignature API, Agreement Manager API, and Workflow Builder API, Docusign offers agreement APIs for a number of other features, including the following:
Web Forms API: Create, manage, and embed Docusign Web Forms.
Connected Fields API: Integrate data verification into Docusign agreements or workflows.
ID Evidence API: Retrieve evidence from a Docusign ID Verification event.
Note: The agreement APIs listed are available in all developer accounts, but only in certain production account plans. Contact Docusign Support
or your account team to find out whether these APIs are available for your production account plan.
Web Forms API
Docusign Web Forms enables you to build web pages that contain fields in which users enter data. User-entered form values can be dynamically incorporated into eSignature envelopes that users sign, as well as exported to your business applications. With the Web Forms builder, you can easily create a sequence of form pages, add form fields, set validation rules, and apply conditional logic.
Web Forms API
The Web Forms API enables you to create and integrate the web form instances that users fill out. You can also use the API to retrieve data about the web form configurations that are available in your Docusign account.
In addition to the Web Forms API, Docusign provides a JavaScript client SDK, Docusign JS, that you can use to seamlessly embed a web form instance into your website.
Business Use Cases
Financial Aid Application
Robin is a developer for a university. An administrator created a form using Docusign Web Forms that students can complete to start the process of applying for financial aid each term. Robin used the Web Forms API to integrate this form into the university's website so students can complete the form and then sign the application while they're using the site.
Insurance Claims
Connected Fields API
Docusign data verification enables you to verify signer-provided information in real time with trusted databases. Implementing data verification avoids the need to correct data later, reducing costs and accelerating your agreement processes.
You can use Basic or Premium data verification to verify several common types of data using sources integrated with Docusign. You can also implement Custom data verification to securely verify data against internal systems or other authoritative data sources that you choose.
Connected Fields API
When you implement data verification in your custom apps, you can use the Connected Fields API to get information on the connected fields that your agreements use. The API provides the data model for each extension app that supports data verification or connected fields. Your integration can then use the data model to add the fields to your agreements and present them for signature.
ID Evidence API
Docusign ID Verification solutions enable you to authenticate and verify recipients' identities before they can review and sign their documents or as they complete workflow steps.
Docusign offers different variations of Docusign ID Verification to align with your specific needs. Different ID Verification configurations offer different verification methods.
For example, with the standard Docusign ID Verification configuration, recipients must identify themselves by providing an image of a valid government-issued photo ID, using an electronic or bank ID, using a CLEAR account (US residents only), or by going through knowledge-based authentication (US residents only).
ID Evidence API
Your account administrator can choose to configure your Docusign account to retain one or more types of ID Verification data. You can then use the ID Evidence API to retrieve the selected information about an ID verification event after an agreement participant successfully completes ID verification. For instance, for photo IDs your administrator can choose to make ID images available, as well as personal information and document details.
What Tools Are Available for Docusign Agreement API Developers?
→ Docusign provides several free tools and resources to help developers build integrations using Docusign Agreement APIs more efficiently, including SDKs and Quickstart.
SDKs
Docusign SDKs wrap Agreement APIs with objects, properties, and methods in your favorite programming language. SDKs are available for development in C#, Java, Node.js, PHP, Python, and Ruby.
SDKS
Quickstart
Docusign Quickstart is a free tool from Docusign that generates a code project, in your choice of Bash, C#, Java, Node.js, PHP, Python, PowerShell or Ruby, that is preconfigured with all the personalized developer account and OAuth implementation settings that you need to get started developing Docusign integrations.
QUICKSTART TOOL
Sample Apps
Try out sample apps that demonstrate common agreement API workflows and showcase best practices around implementation.
Other Tools
The Docusign Developer Center also offers additional tools and resources including an API explorer, a Postman collection, an OpenAPI specification, and IDE extensions for both Visual Studio Code and Visual Studio.
TOOLS OVERVIEW
Lesson 6 - Create Workflows

Docusign for Developers Overview
Introduction to Docusign for Developers
AGREEMENT APIS
Integrate Signing with the eSignature API
Integrate Agreement Data with the Agreement Manager API
Integrate Workflows with the Workflow Builder API
Integrate More Features with Additional Agreement APIs
WORKFLOWS
Create Workflows
EXTENSION APPS
Integrate External Features with Extension Apps
Scenario: Plan Docusign Integrations
Lesson 4 - Integrate Workflows with the Workflow Builder API
Integrate More Features with Additional Agreement APIs
Objective: After reviewing this topic, you will be able to identify additional Docusign agreement APIs and describe use cases each one supports for custom integrations.
In addition to the eSignature API, Agreement Manager API, and Workflow Builder API, Docusign offers agreement APIs for a number of other features, including the following:
Web Forms API: Create, manage, and embed Docusign Web Forms.
Connected Fields API: Integrate data verification into Docusign agreements or workflows.
ID Evidence API: Retrieve evidence from a Docusign ID Verification event.
Note: The agreement APIs listed are available in all developer accounts, but only in certain production account plans. Contact Docusign Support
or your account team to find out whether these APIs are available for your production account plan.
Web Forms API
Docusign Web Forms enables you to build web pages that contain fields in which users enter data. User-entered form values can be dynamically incorporated into eSignature envelopes that users sign, as well as exported to your business applications. With the Web Forms builder, you can easily create a sequence of form pages, add form fields, set validation rules, and apply conditional logic.
Web Forms API
The Web Forms API enables you to create and integrate the web form instances that users fill out. You can also use the API to retrieve data about the web form configurations that are available in your Docusign account.
In addition to the Web Forms API, Docusign provides a JavaScript client SDK, Docusign JS, that you can use to seamlessly embed a web form instance into your website.
Business Use Cases
Financial Aid Application
Robin is a developer for a university. An administrator created a form using Docusign Web Forms that students can complete to start the process of applying for financial aid each term. Robin used the Web Forms API to integrate this form into the university's website so students can complete the form and then sign the application while they're using the site.
Insurance Claims
William is a developer for an insurance company. He built a form using Docusign Web Forms for customers to provide information about new claims. His integration calls the Web Forms API to pre-populate form fields with basic customer information pulled from the company's other systems, so users only have to complete the fields specific to the claim they are filing.
Connected Fields API
Docusign data verification enables you to verify signer-provided information in real time with trusted databases. Implementing data verification avoids the need to correct data later, reducing costs and accelerating your agreement processes.
You can use Basic or Premium data verification to verify several common types of data using sources integrated with Docusign. You can also implement Custom data verification to securely verify data against internal systems or other authoritative data sources that you choose.
Connected Fields API
When you implement data verification in your custom apps, you can use the Connected Fields API to get information on the connected fields that your agreements use. The API provides the data model for each extension app that supports data verification or connected fields. Your integration can then use the data model to add the fields to your agreements and present them for signature.
ID Evidence API
Docusign ID Verification solutions enable you to authenticate and verify recipients' identities before they can review and sign their documents or as they complete workflow steps.
Docusign offers different variations of Docusign ID Verification to align with your specific needs. Different ID Verification configurations offer different verification methods.
For example, with the standard Docusign ID Verification configuration, recipients must identify themselves by providing an image of a valid government-issued photo ID, using an electronic or bank ID, using a CLEAR account (US residents only), or by going through knowledge-based authentication (US residents only).
ID Evidence API
Your account administrator can choose to configure your Docusign account to retain one or more types of ID Verification data. You can then use the ID Evidence API to retrieve the selected information about an ID verification event after an agreement participant successfully completes ID verification. For instance, for photo IDs your administrator can choose to make ID images available, as well as personal information and document details.
What Tools Are Available for Docusign Agreement API Developers?
→ Docusign provides several free tools and resources to help developers build integrations using Docusign Agreement APIs more efficiently, including SDKs and Quickstart.
SDKs
Docusign SDKs wrap Agreement APIs with objects, properties, and methods in your favorite programming language. SDKs are available for development in C#, Java, Node.js, PHP, Python, and Ruby.
SDKS
Quickstart
Docusign Quickstart is a free tool from Docusign that generates a code project, in your choice of Bash, C#, Java, Node.js, PHP, Python, PowerShell or Ruby, that is preconfigured with all the personalized developer account and OAuth implementation settings that you need to get started developing Docusign integrations.
QUICKSTART TOOL
Sample Apps
Try out sample apps that demonstrate common agreement API workflows and showcase best practices around implementation.
Other Tools
The Docusign Developer Center also offers additional tools and resources including an API explorer, a Postman collection, an OpenAPI specification, and IDE extensions for both Visual Studio Code and Visual Studio.
TOOLS OVERVIEW
Lesson 6 - Create Workflows

Docusign for Developers Overview
Introduction to Docusign for Developers
AGREEMENT APIS
Integrate Signing with the eSignature API
Integrate Agreement Data with the Agreement Manager API
Integrate Workflows with the Workflow Builder API
Integrate More Features with Additional Agreement APIs
WORKFLOWS
Create Workflows
EXTENSION APPS
Integrate External Features with Extension Apps
Scenario: Plan Docusign Integrations
Create Workflows
Objective: After reviewing this topic, you will be able to describe common use cases and resources for creating a workflow.
Note: workflows are available in all developer accounts, but only in certain production account plants. Contact Docusign Support
or your account team to find out whether workflows are available for your production account plan.
Workflow Builder
With Workflow Builder you can create workflows to automate business processes. Workflows offer basic conditionality, and support modules including ID Verification, Web Forms, Sign, and CLM, as well as partner applications from a variety of third-party services like ServiceNow, Stripe, and Google Drive.
Workflow Builder enables you to monitor workflows for visibility into user data, where they are in the process, and where they may be dropping off.
Business Use Cases
Property Sale
New Customer Intake
Workflows Development Process Overview
To build a workflow, you follow these steps in Workflow Builder:
1
Specify participants and any starting variables.
2
Add a step from the available options, then configure options for your step.
3
Continue to add steps until your workflow is complete.
4
Provide a name for your workflow, resolve any variable errors, then publish your workflow.
To learn how to create workflows, click the link for your account type, then register for the Docusign University course Build Agreement Workflows with Docusign (Customer
| Developer/Demo
| Employee
| Partner
)
Note: The Docusign Template Library offers pre-configured workflow samples to help you start building your own workflows.
| Developer/Demo
| Employee
| Partner
Integrate More Features with Additional Agreement APIs
Objective: After reviewing this topic, you will be able to identify additional Docusign agreement APIs and describe use cases each one supports for custom integrations.
In addition to the eSignature API, Agreement Manager API, and Workflow Builder API, Docusign offers agreement APIs for a number of other features, including the following:
Web Forms API: Create, manage, and embed Docusign Web Forms.
Connected Fields API: Integrate data verification into Docusign agreements or workflows.
ID Evidence API: Retrieve evidence from a Docusign ID Verification event.
Note: The agreement APIs listed are available in all developer accounts, but only in certain production account plans. Contact Docusign Support
or your account team to find out whether these APIs are available for your production account plan.
Web Forms API
Docusign Web Forms enables you to build web pages that contain fields in which users enter data. User-entered form values can be dynamically incorporated into eSignature envelopes that users sign, as well as exported to your business applications. With the Web Forms builder, you can easily create a sequence of form pages, add form fields, set validation rules, and apply conditional logic.
Web Forms API
The Web Forms API enables you to create and integrate the web form instances that users fill out. You can also use the API to retrieve data about the web form configurations that are available in your Docusign account.
In addition to the Web Forms API, Docusign provides a JavaScript client SDK, Docusign JS, that you can use to seamlessly embed a web form instance into your website.
Business Use Cases
Financial Aid Application
Robin is a developer for a university. An administrator created a form using Docusign Web Forms that students can complete to start the process of applying for financial aid each term. Robin used the Web Forms API to integrate this form into the university's website so students can complete the form and then sign the application while they're using the site.
Insurance Claims
William is a developer for an insurance company. He built a form using Docusign Web Forms for customers to provide information about new claims. His integration calls the Web Forms API to pre-populate form fields with basic customer information pulled from the company's other systems, so users only have to complete the fields specific to the claim they are filing.
Connected Fields API
Docusign data verification enables you to verify signer-provided information in real time with trusted databases. Implementing data verification avoids the need to correct data later, reducing costs and accelerating your agreement processes.
You can use Basic or Premium data verification to verify several common types of data using sources integrated with Docusign. You can also implement Custom data verification to securely verify data against internal systems or other authoritative data sources that you choose.
Connected Fields API
When you implement data verification in your custom apps, you can use the Connected Fields API to get information on the connected fields that your agreements use. The API provides the data model for each extension app that supports data verification or connected fields. Your integration can then use the data model to add the fields to your agreements and present them for signature.
ID Evidence API
Docusign ID Verification solutions enable you to authenticate and verify recipients' identities before they can review and sign their documents or as they complete workflow steps.
Docusign offers different variations of Docusign ID Verification to align with your specific needs. Different ID Verification configurations offer different verification methods.
For example, with the standard Docusign ID Verification configuration, recipients must identify themselves by providing an image of a valid government-issued photo ID, using an electronic or bank ID, using a CLEAR account (US residents only), or by going through knowledge-based authentication (US residents only).
ID Evidence API
Your account administrator can choose to configure your Docusign account to retain one or more types of ID Verification data. You can then use the ID Evidence API to retrieve the selected information about an ID verification event after an agreement participant successfully completes ID verification. For instance, for photo IDs your administrator can choose to make ID images available, as well as personal information and document details.
What Tools Are Available for Docusign Agreement API Developers?
→ Docusign provides several free tools and resources to help developers build integrations using Docusign Agreement APIs more efficiently, including SDKs and Quickstart.
SDKs
Docusign SDKs wrap Agreement APIs with objects, properties, and methods in your favorite programming language. SDKs are available for development in C#, Java, Node.js, PHP, Python, and Ruby.
SDKS
Quickstart
Docusign Quickstart is a free tool from Docusign that generates a code project, in your choice of Bash, C#, Java, Node.js, PHP, Python, PowerShell or Ruby, that is preconfigured with all the personalized developer account and OAuth implementation settings that you need to get started developing Docusign integrations.
QUICKSTART TOOL
Sample Apps
Try out sample apps that demonstrate common agreement API workflows and showcase best practices around implementation.
Other Tools
The Docusign Developer Center also offers additional tools and resources including an API explorer, a Postman collection, an OpenAPI specification, and IDE extensions for both Visual Studio Code and Visual Studio.
TOOLS OVERVIEW
Lesson 7 - Integrate External Features with Extension Apps

### Implement Authentication for Docusign APIs 30 min

Implement Authentication for Docusign APIs
Introduction to Docusign API Authentication
AUTHORIZATION CODE GRANT
Confidential and Public Authorization Code Grants
Hands-on Practice
JWT GRANT
JSON Web Token (JWT) Grant
Hands-on Practice
Knowledge Check
Docusign API Authentication Scenarios
Lesson 4 - JSON Web Token (JWT) Grant
Hands-on Practice
Let's walk through the entire JSON Web Token Grant process.
This activity can be completed in 10 minutes.
Setup
To complete this activity, you need a Docusign developer account. If you don't already have one, you can create a developer account
on the Docusign Developer Center.
In your browser, log in to your Docusign developer account.
From the Admin page, click Apps and Keys, then click Add App and Integration Key to create a new app.
Provide a name for your app and click Create App.
Select an Integration Type for your app.
Note: To learn more about the different Integration Types, explore the Docusign Go-live
process on the Docusign Developer Center.
Click Add Secret Key to create a secret key, copy the value, then save it in a secure storage, such as a password/credential manager application.
Click Generate RSA to generate RSA keys, copy both of these keys, then save them in your secure storage, as they will not be displayed again.
Click Add URI, then enter https://mozilla.org
or another website of your choice.
Click Save.
Open the Using the Docusign API Postman collections
page on the Docusign Developer Center and follow the steps to set up your environment and fork or import the Postman collection for at least one Docusign API.
In the Environments list, set Docusign-account-d as the active environment.
Obtain Consent
Note: This activity uses manual consent, not admin consent. You will need to use a browser to complete the first task.
Copy the following URL to your web browser's address bar:
https://account-d.docusign.com/oauth/auth?response_type=code&scope=signature%20impersonation&client_id={{integrationKey}}&redirect_uri=https://mozilla.org
Replace {{integrationKey}} with your application's integration key, and if necessary replace https://mozilla.org with the redirect URI that you configured for your app in Docusign eSignature.
https://account-d.docusign.com/oauth/auth?response_type=code&scope=signature%20impersonation&client_id=7b22cb84-xxxx-xxxx-xxxx-6bfa579058ea&redirect_uri=https://mozilla.org
Press Enter to navigate to the URL.
Log in to your Docusign developer account and give consent. After you click Allow Access to give the application permission, you will be redirected to your redirect URI.
Create a JWT
You will use a tool called JWT.io to create and validate the JWT. This tool is an online debugger that validates JSON web tokens.
You will also need both your private and public RSA keys to complete this step.
Note: While we use JWT.io
in this demonstration to visualize the structure of a JSON Web Token, remember that this tool is intended for learning and debugging purposes only. For a production environment, you must use one of the following secure methods:
Docusign SDKs: Integrate the Docusign SDKs for secure handling of JSON Web Tokens.
Language-Specific Libraries: Use the secure, built-in cryptographic tools provided by the programming language you are using.
Construct the Header
Open https://jwt.io
in another tab or window, then click JWT Encoder to open the encoder tab.
Select the following header code:
{
"alg": "RS256",
"typ": "JWT"
}
JWT header object
Replace the contents of the Header section with the code you copied.
Construct the Payload
Select the following schema code and copy it to the clipboard, then go to the JWT tool, delete the contents of the Payload section, and paste the code you copied.
{
"iss": "{YOUR INTEGRATION KEY}",
"sub": "{YOUR USER ID}",
"iat": {YOUR ISSUE DATE},
"exp": {YOUR EXP DATE},
"aud": "{URI}",
"scope": "{LIST OF SCOPES}"
}
JWT payload schema
In another browser tab or window, log into your Docusign Developer account, select Admin, select Apps and Keys, then copy the value of the integration key for your app to the clipboard.
Go to the JWT tool, delete the placeholder value for the iss property, then paste the integration key you copied between double quotes as the iss value.
Return to your Docusign Developer account in another browser tab or window, select Admin, select Apps and Keys, then copy the User ID value to the clipboard.
Go to the JWT tool, delete the placeholder value for the sub property, then paste the User ID value you copied between double quotes as the sub value.
Open your browser console, at the command prompt enter Math.floor(Date.now()/1000), then copy the result to the clipboard.
This statement returns a ten-digit number that represents the current date and time in seconds Unix epoch format.
Go to the JWT tool again and replace the placeholder value for the iat property with the value you copied from the console.
At the command prompt in your browser console, paste the iat value you previously generated, type + 3600 after it, press Enter, then copy the result to the clipboard.
This statement returns a date and time exactly one hour (3600 seconds) after the issue date you previously generated.
Go to the JWT tool again and replace the placeholder value for the exp property with the value you copied from the console.
Still in the JWT tool, replace the value for the aud property with account-d.docusign.com between quotes.
Note: This exercise uses the aud URI for the account-d.docusign.com development environment. In production, you must change this value to account.docusign.com.
Delete the placeholder value for the scope property, then enter signature between quotes as the scope value.
Note: The scope value is different from the scope permissions used earlier during the consent step. After permission is granted, you no longer need to request impersonation scope. Instead, the scope value in your JWT payload should contain only the scope or scopes your app will need for the APIs you will call. This exercise requests only signature scope.
In the JWT tool, verify if the message Valid payload is displayed and the Payload pane becomes green, then the payload you entered is valid JSON.
If the background of the Payload section instead shows a red color, check your payload syntax against the previous steps and correct any errors.
Construct the Signature
In your secure storage application, select and copy the RSA Private Key for your Docusign app.
In the JWT tool, paste your private key in the Sign JWT section.
If your header, payload, and private key are valid, a "Valid private key" message is displayed. If you instead see an error message, verify that you pasted your private RSA key, including the "-----BEGIN RSA PRIVATE KEY-----" and "-----END RSA PRIVATE KEY-----" lines, and did not include quotes.
When all three fields are complete, the tool automatically generates a JSON web token on the right side of the screen. Note that you may need to scroll up to view the JWT.
Click the Copy button for the JSON web token to copy it to your clipboard.
You will use this encoded value in the next step of the JWT Grant flow to request an access token.
Acquire an Access Token
In Postman, open the collection for a Docusign API, then open the Authentication section.
Select the 02 JWT Access Token request, then select the Body tab.
Replace the placeholder value for the assertion key with the JWT you copied from the JWT.io tool.
Click Send to send the request.
Verify that your response contains an access_token value.
Note: Docusign REST API Postman collections include post-request scripts that automatically update environment variables in Postman based on response data. As a result, your access token is stored in your Postman environment for you, and your subsequent JSON Web Token Grant calls will work without requiring you to perform any additional configuration.
Acquire User Information
Within the Authentication section of the Postman collection, open the 04 Get User Info request.
Select the Headers tab. The request includes the Authorization header with a value of Bearer followed by the environment variable that stores your access token.
Click Send to send the request.
Your response includes account_id and base_uri values within each object in the accounts array.
Now that you have acquired an access token and user information, you have everything you need to make authenticated calls to Docusign APIs within the scopes you specified for your JWT.
Lesson 6 - Knowledge Check

Implement Authentication for Docusign APIs
RESUME COURSE
Welcome to the Implement API Authentication for Docusign APIs course. After reviewing this course, you will be able to:
Describe the OAuth 2.0 authentication flows supported by Docusign APIs.
Authenticate a web application to Docusign using the Authorization Code Grant flow.
Authenticate a web application or service integration to Docusign using the JSON Web Token (JWT) Grant flow.
Introduction to Docusign API Authentication
AUTHORIZATION CODE GRANT
Confidential and Public Authorization Code Grants
Hands-on Practice
JWT GRANT
JSON Web Token (JWT) Grant
Hands-on Practice
Knowledge Check
Docusign API Authentication Scenarios

Implement Authentication for Docusign APIs
Introduction to Docusign API Authentication
AUTHORIZATION CODE GRANT
Confidential and Public Authorization Code Grants
Hands-on Practice
JWT GRANT
JSON Web Token (JWT) Grant
Hands-on Practice
Knowledge Check
Docusign API Authentication Scenarios
Confidential and Public Authorization Code Grants
Objective: After reviewing this topic, you will be able to implement the Docusign Confidential Authorization Code Grant and Public Authorization Code Grant authentication flows.
Authorization Code Grant (Auth Code Grant) is an OAuth 2.0 authentication flow that Docusign APIs support to verify your application's identity and confirm its authorization to act on behalf of a specific user. This flow is ideal for web applications where a user interacts with the application and authenticates using their individual Docusign login.
Docusign offers two versions of auth code grant:
1
Confidential Auth Code Grant: Recommended for server-hosted applications that can securely store a secret key.
2
Public Auth Code Grant: Recommended for single-page applications (SPAs) and native apps that cannot securely store a secret key. This grant flow uses Proof Key for Code Exchange (PKCE) for security.
Both flows require an integration key and a redirect URI configured in eSignature Admin.
Configure Authentication Settings
Before building your authentication flow, you must specify the type of Auth Code Grant your app will use in Docusign Admin:
From your Docusign account, click the Admin tab.
Select Apps and Keys.
If you are starting a new app, click Add App and Integration Key.
OR
If you have already started building your app, select the Actions menu for the app you want to configure, then select Edit.
The app settings page enables you to specify the auth type for your app.
•
For Confidential Auth Code Grant, indicate that your app can securely store a client secret. This is the default setting. You will add a secret key in your app's authentication settings.
•
For Public Auth Code Grant, indicate that your app cannot securely store a client secret and specify whether it's a single-page web application or a native OS application. These settings enable Authorization Code Grant with PKCE.
The Auth Code Grant flow involves three main steps, which must be completed in a specific order, followed by an optional step for token renewal:
Acquire an Authorization Code
Acquire Tokens (Access Token and Refresh Token)
Acquire User Information
Refresh Tokens
Step 1: Acquire an Authorization Code
In this step, your application navigates to a URI to request an authorization code using query string parameters.
Users are prompted to log in and allow access. By doing so, they give permission for Docusign services to authenticate and grant access on their behalf.
This avoids requiring users to approve access to a system every time authorization code or token requests are made in the future.
Base URI
Docusign development and production endpoints use different domains. As a result, the base URI for Docusign authentication varies depending on whether your app is in development or is deployed to production:
Development
https://account-d.docusign.com/oauth/auth
Production
https://account.docusign.com/oauth/auth
Note: All examples in this course use development endpoints. When deploying your app to production, ensure that you update all instances of the URI to use production endpoints.
Required Query String Parameters
Redirect the user's browser to a constructed Docusign authentication URI.
Your HTTP request to the URI must include the following four query string parameters:
•
client_id: Your application's integration key.
•
redirect_uri: The URI where Docusign will redirect the user after consent is given, delivering the authorization code. This must be pre-configured with your integration key.
•
scope: One or more scopes necessary for the API actions your integration will perform, such as signature for most eSignature API actions. The extended scope enables a long refresh token lifecycle.
•
response_type: The value code.
Optional Query String Parameters
Both Auth Code Grant flows also support two optional query parameters:
•
code_challenge and code_challenge_method: For all Public Auth Code Grant implementations, as well as Confidential Auth Code Grant implementations that use PKCE, these parameters verify that the app that starts the flow is the one that finishes it.
To create the value of the code_challenge parameter, your app must generate a cryptographically random string, hash that string with the S256 algorithm, then base64 URL-encode it.
The value of the code_challenge_method parameter is always S256.
These parameters are required when you use the Public Auth Code Grant flow
•
state: Include a state parameter with a random string to prevent Cross-Site Request Forgery (CSRF) attacks.
Response
After the user logs in and grants consent, Docusign redirects back to your redirect_uri, including a code query string parameter containing the authorization code.
https://example.com?code=eyJ0eXAiOiJNVCIs...
Note: This authorization code is only valid for 120 seconds (2 minutes). You must use it in the next step within this timeframe, or it will expire. If your authorization code expires, resubmit the consent url to regenerate the code.
Step 2: Acquire Tokens
Once you have the authorization code, your application can programmatically request access and refresh tokens without further user interaction.
Method and endpoint
POST /oauth/token
Header
For a Confidential Auth Code Grant request, you must base64-encode your integration key followed by a comma and your secret key. You then pass this value in a header with the following syntax:
Authorization: Basic {{encodedKeys}}
To generate the encoded value, you base64-encode a string that consists of your integration key followed by a colon and then your secret key, with no spaces:
integrationKey:secretKey
For example, the following JavaScript code generates a base64 encoded value based on placeholder integration and secret keys:
Note: The header containing encoded keys is required only for Confidential Auth Code Grant. For a Public Auth Code Grant implementation, you instead provide a code_verifier value in the body.
•
code: The authorization code obtained in Step 1.
•
grant_type: authorization_code.
•
client_id: Your application's integration key.
•
code_verifier: The random string you generated to create the code_challenge value when you acquired an authorization code. (Required only for Public Auth Code Grant.)
Required Body Parameters
The following snippet shows a raw HTTP request for tokens to the Docusign authentication service for a Confidential Auth Code Grant implementation:
Response
The response provides an access token (valid for 8 hours) and a refresh token. The refresh token is valid for up to 30 days for Confidential Auth Code Grant and 24 hours for Public Auth Code Grant.
Step 3: Acquire User Information
After obtaining tokens, you need to retrieve specific user account information necessary for making Docusign API calls. This step is crucial because Docusign API request URIs include the user's account ID and base URI.
Method and endpoint
GET /oauth/userinfo
Required Header
Authorization: Bearer {{accessToken}}
Response
The response contains an accounts array. You'll typically use the account with is_default set to true. From the selected account object, extract the account_id and base_uri values, which are essential for constructing all subsequent Docusign API requests.
Step 4: Refresh Tokens
Access tokens expire after 8 hours, but your integration can use a refresh token to obtain a new access token. This enables you to extend application access without requiring users to log in repeatedly.
Method and endpoint
POST /oauth/token
Required Header
Authorization: Basic {{encodedKeys}}
Note: The header containing encoded keys is required only for Confidential Auth Code Grant. For a Public Auth Code Grant implementation, you instead provide a code_verifier value in the body.
Required Body Parameters
•
grant_type: refresh_token
•
client_id: Your application's integration key.
•
refresh_token: The refresh token obtained in Step 2.
•
code_verifier: The random string you generated to create the code_challenge value when you acquired an authorization code. (Required only for Public Auth Code Grant.)
Response
You will receive a new access token and a new refresh token. The previous access token is no longer valid.
The snippet below shows a raw HTTP request to refresh tokens to the Docusign authentication service for a Confidential Auth Code Grant implementation:
Refresh Token Lifecycles
•
With basic permission scopes (e.g., signature only), the refresh token expires 30 days from its original issue date.
•
With the extended scope, the refresh token expires 30 days from the last successful refresh date, allowing for continuous access.
Best Practice
Evaluate your application's security posture before implementing the extended scope due to the longer token validity periods.
Knowledge Check
Which statement accurately describes a key characteristic of the Authorization Code Grant OAuth 2.0 flow for Docusign APIs?
It is ideal for automated service integrations without individual user interaction.
It is specifically designed for web applications where a user interacts with the application and authenticates on an individual basis.
It does not require an authorization code, resulting in fewer authentication steps.
SUBMIT
Incorrect
TAKE AGAIN
For what type of application or integration is the JSON Web Token (JWT) Grant OAuth 2.0 flow the best choice?
Server-hosted applications designed for users with individual Docusign accounts.
Single-page apps and native mobile apps that cannot securely store a secret.
Automated service integrations that do not require individual user login.
SUBMIT
Incorrect
TAKE AGAIN
For the Confidential Authorization Code Grant Flow, where is the access token typically stored?
On the server.
In application memory.
In an external database.
SUBMIT
Incorrect
TAKE AGAIN
Before an application using JWT Grant can impersonate an admin user to make API calls, what must first be obtained?
The admin user's consent, typically as a one-time step.
A random string for the code challenge value.
A client secret from the Docusign Admin page.
SUBMIT
Incorrect
TAKE AGAIN
What crucial pieces of user account information are retrieved from the /userinfo endpoint that are essential for constructing all subsequent Docusign API requests, regardless of the OAuth flow used?
access_token and refresh_token
account_id and base_uri
client_id and redirect_uri
SUBMIT
Incorrect
TAKE AGAIN
Lesson 3 - Hands-on Practice

Implement Authentication for Docusign APIs
Introduction to Docusign API Authentication
AUTHORIZATION CODE GRANT
Confidential and Public Authorization Code Grants
Hands-on Practice
JWT GRANT
JSON Web Token (JWT) Grant
Hands-on Practice
Knowledge Check
Docusign API Authentication Scenarios
Hands-on Practice
Let's walk through the entire Confidential Authorization Code Grant process.
This activity can be completed in 10 minutes.
Setup
To complete this activity, you need a Docusign developer account. If you don't already have one, you can create a developer account
on the Docusign Developer Center.
In your browser, log in to your Docusign developer account.
From the Admin page, click Apps and Keys, then click Add App and Integration Key to create a new app.
Provide a name for your app and click Create App.
Select an Integration Type for your app.
Note: To learn more about the different integration types, explore the Docusign Go-live
process on the Docusign Developer Center.
Click Add Secret Key to create a secret key, copy the value, then save it in secure storage, such as a password/credential manager application.
Click Add URI, then enter https://mozilla.org
or another website of your choice.
Click Save.
Open the Using the Docusign API Postman collections
page on the Docusign Developer Center and follow the steps to set up your environment and fork or import the Postman collection for at least one Docusign API.
In the Environments list, set Docusign-account-d as the active environment.
Acquire an Authorization Code
Copy the following URL to your web browser's address bar:
https://account-d.docusign.com/oauth/auth?response_type=code&scope=signature&client_id={{integrationKey}}&redirect_uri=https://mozilla.org
Replace {{integrationKey}} with your application's integration key, and if necessary replace https://mozilla.org with the redirect URI that you configured for your app in eSignature Admin.
https://account-d.docusign.com/oauth/auth?response_type=code&scope=signature&client_id=7b22cb84-xxxx-xxxx-xxxx-6bfa579058ea&redirect_uri=https://mozilla.org
Press Enter to navigate to the URL.
Log in to your Docusign developer account and give consent. After you click Allow Access to give the application permission, you will be redirected to your redirect URI.
In the URI in your browser's address bar, select the value of the code parameter at the end of the URI (everything after the equal sign). Note that the entire code value probably will not fit on the screen, so be sure to scroll all the way to the end of the URI to capture the entire value.
Note: After the URI loads in your browser, you have only 120 seconds (2 minutes) to complete the next task in the activity before the code expires.
Acquire Tokens
In Postman, open the collection for a Docusign API, then open the Authentication section.
Open the 01 Authorize Code Grant Access Token request, then select the Body tab.
Replace the placeholder value for the code parameter {{codeFromUrl}} with the value you copied from the URI.
Click Send to send the request.
Verify that your response includes access_token, token_type, refresh_token, expires_in, and scope values.
Note: Docusign REST API Postman collections include post-request scripts that automatically update environment variables in Postman based on response data. As a result, tokens are stored in your Postman environment for you, and your subsequent Authorization Code Grant calls will work without requiring you to perform any additional configuration.
Acquire User Information
Within the Authentication section of the Postman collection, open the 04 Get User Info request.
Select the Headers tab. The request includes the Authorization header with a value of Bearer followed by the environment variable that stores your access token.
Click Send to send the request.
Your response includes account_id and base_uri values within each object in the accounts array.
Now that you have acquired an access token and user information, you have everything you need to make authenticated calls to Docusign APIs within the scopes you specified in your initial authorization code request.
Refresh Tokens
Within the Authentication section of the Postman collection, open the 03 Refresh Access Token request.
Select the Headers tab. The request includes the Authorization header with a value of Basic followed by the environment variable that stores your encoded keys.
Select the Body tab. The request includes the refresh_token key with a value equal to the environment variable that stores your refresh token. It also includes a grant_type key with a string value of refresh_token.
Click Send to send the request.
Your response includes new access_token and refresh_token values.
Confidential and Public Authorization Code Grants
Objective: After reviewing this topic, you will be able to implement the Docusign Confidential Authorization Code Grant and Public Authorization Code Grant authentication flows.
Authorization Code Grant (Auth Code Grant) is an OAuth 2.0 authentication flow that Docusign APIs support to verify your application's identity and confirm its authorization to act on behalf of a specific user. This flow is ideal for web applications where a user interacts with the application and authenticates using their individual Docusign login.
Docusign offers two versions of auth code grant:
1
Confidential Auth Code Grant: Recommended for server-hosted applications that can securely store a secret key.
2
Public Auth Code Grant: Recommended for single-page applications (SPAs) and native apps that cannot securely store a secret key. This grant flow uses Proof Key for Code Exchange (PKCE) for security.
Both flows require an integration key and a redirect URI configured in eSignature Admin.
Configure Authentication Settings
Before building your authentication flow, you must specify the type of Auth Code Grant your app will use in Docusign Admin:
From your Docusign account, click the Admin tab.
Select Apps and Keys.
If you are starting a new app, click Add App and Integration Key.
OR
If you have already started building your app, select the Actions menu for the app you want to configure, then select Edit.
The app settings page enables you to specify the auth type for your app.
•
For Confidential Auth Code Grant, indicate that your app can securely store a client secret. This is the default setting. You will add a secret key in your app's authentication settings.
•
For Public Auth Code Grant, indicate that your app cannot securely store a client secret and specify whether it's a single-page web application or a native OS application. These settings enable Authorization Code Grant with PKCE.
The Auth Code Grant flow involves three main steps, which must be completed in a specific order, followed by an optional step for token renewal:
Acquire an Authorization Code
Acquire Tokens (Access Token and Refresh Token)
Acquire User Information
Refresh Tokens
Step 1: Acquire an Authorization Code
In this step, your application navigates to a URI to request an authorization code using query string parameters.
Users are prompted to log in and allow access. By doing so, they give permission for Docusign services to authenticate and grant access on their behalf.
This avoids requiring users to approve access to a system every time authorization code or token requests are made in the future.
Base URI
Docusign development and production endpoints use different domains. As a result, the base URI for Docusign authentication varies depending on whether your app is in development or is deployed to production:
Development
https://account-d.docusign.com/oauth/auth
Production
https://account.docusign.com/oauth/auth
Note: All examples in this course use development endpoints. When deploying your app to production, ensure that you update all instances of the URI to use production endpoints.
Required Query String Parameters
Redirect the user's browser to a constructed Docusign authentication URI.
Your HTTP request to the URI must include the following four query string parameters:
•
client_id: Your application's integration key.
•
redirect_uri: The URI where Docusign will redirect the user after consent is given, delivering the authorization code. This must be pre-configured with your integration key.
•
scope: One or more scopes necessary for the API actions your integration will perform, such as signature for most eSignature API actions. The extended scope enables a long refresh token lifecycle.
•
response_type: The value code.
Optional Query String Parameters
Both Auth Code Grant flows also support two optional query parameters:
•
code_challenge and code_challenge_method: For all Public Auth Code Grant implementations, as well as Confidential Auth Code Grant implementations that use PKCE, these parameters verify that the app that starts the flow is the one that finishes it.
To create the value of the code_challenge parameter, your app must generate a cryptographically random string, hash that string with the S256 algorithm, then base64 URL-encode it.
The value of the code_challenge_method parameter is always S256.
These parameters are required when you use the Public Auth Code Grant flow
•
state: Include a state parameter with a random string to prevent Cross-Site Request Forgery (CSRF) attacks.
Response
After the user logs in and grants consent, Docusign redirects back to your redirect_uri, including a code query string parameter containing the authorization code.
https://example.com?code=eyJ0eXAiOiJNVCIs...
Note: This authorization code is only valid for 120 seconds (2 minutes). You must use it in the next step within this timeframe, or it will expire. If your authorization code expires, resubmit the consent url to regenerate the code.
Step 2: Acquire Tokens
Once you have the authorization code, your application can programmatically request access and refresh tokens without further user interaction.
Method and endpoint
POST /oauth/token
Header
For a Confidential Auth Code Grant request, you must base64-encode your integration key followed by a comma and your secret key. You then pass this value in a header with the following syntax:
Authorization: Basic {{encodedKeys}}
To generate the encoded value, you base64-encode a string that consists of your integration key followed by a colon and then your secret key, with no spaces:
integrationKey:secretKey
For example, the following JavaScript code generates a base64 encoded value based on placeholder integration and secret keys:
Note: The header containing encoded keys is required only for Confidential Auth Code Grant. For a Public Auth Code Grant implementation, you instead provide a code_verifier value in the body.
•
code: The authorization code obtained in Step 1.
•
grant_type: authorization_code.
•
client_id: Your application's integration key.
•
code_verifier: The random string you generated to create the code_challenge value when you acquired an authorization code. (Required only for Public Auth Code Grant.)
Required Body Parameters
The following snippet shows a raw HTTP request for tokens to the Docusign authentication service for a Confidential Auth Code Grant implementation:
Response
The response provides an access token (valid for 8 hours) and a refresh token. The refresh token is valid for up to 30 days for Confidential Auth Code Grant and 24 hours for Public Auth Code Grant.
Step 3: Acquire User Information
After obtaining tokens, you need to retrieve specific user account information necessary for making Docusign API calls. This step is crucial because Docusign API request URIs include the user's account ID and base URI.
Method and endpoint
GET /oauth/userinfo
Required Header
Authorization: Bearer {{accessToken}}
Response
The response contains an accounts array. You'll typically use the account with is_default set to true. From the selected account object, extract the account_id and base_uri values, which are essential for constructing all subsequent Docusign API requests.
Step 4: Refresh Tokens
Access tokens expire after 8 hours, but your integration can use a refresh token to obtain a new access token. This enables you to extend application access without requiring users to log in repeatedly.
Method and endpoint
POST /oauth/token
Required Header
Authorization: Basic {{encodedKeys}}
Note: The header containing encoded keys is required only for Confidential Auth Code Grant. For a Public Auth Code Grant implementation, you instead provide a code_verifier value in the body.
Required Body Parameters
•
grant_type: refresh_token
•
client_id: Your application's integration key.
•
refresh_token: The refresh token obtained in Step 2.
•
code_verifier: The random string you generated to create the code_challenge value when you acquired an authorization code. (Required only for Public Auth Code Grant.)
Response
You will receive a new access token and a new refresh token. The previous access token is no longer valid.
The snippet below shows a raw HTTP request to refresh tokens to the Docusign authentication service for a Confidential Auth Code Grant implementation:
Refresh Token Lifecycles
•
With basic permission scopes (e.g., signature only), the refresh token expires 30 days from its original issue date.
•
With the extended scope, the refresh token expires 30 days from the last successful refresh date, allowing for continuous access.
Best Practice
Evaluate your application's security posture before implementing the extended scope due to the longer token validity periods.
Lesson 4 - JSON Web Token (JWT) Grant

Implement Authentication for Docusign APIs
Introduction to Docusign API Authentication
AUTHORIZATION CODE GRANT
Confidential and Public Authorization Code Grants
Hands-on Practice
JWT GRANT
JSON Web Token (JWT) Grant
Hands-on Practice
Knowledge Check
Docusign API Authentication Scenarios
Lesson 2 - Confidential and Public Authorization Code Grants
Hands-on Practice
Let's walk through the entire Confidential Authorization Code Grant process.
This activity can be completed in 10 minutes.
Setup
To complete this activity, you need a Docusign developer account. If you don't already have one, you can create a developer account
on the Docusign Developer Center.
In your browser, log in to your Docusign developer account.
From the Admin page, click Apps and Keys, then click Add App and Integration Key to create a new app.
Provide a name for your app and click Create App.
Select an Integration Type for your app.
Note: To learn more about the different integration types, explore the Docusign Go-live
process on the Docusign Developer Center.
Click Add Secret Key to create a secret key, copy the value, then save it in secure storage, such as a password/credential manager application.
Click Add URI, then enter https://mozilla.org
or another website of your choice.
Click Save.
Open the Using the Docusign API Postman collections
page on the Docusign Developer Center and follow the steps to set up your environment and fork or import the Postman collection for at least one Docusign API.
In the Environments list, set Docusign-account-d as the active environment.
Acquire an Authorization Code
Copy the following URL to your web browser's address bar:
https://account-d.docusign.com/oauth/auth?response_type=code&scope=signature&client_id={{integrationKey}}&redirect_uri=https://mozilla.org
Replace {{integrationKey}} with your application's integration key, and if necessary replace https://mozilla.org with the redirect URI that you configured for your app in eSignature Admin.
https://account-d.docusign.com/oauth/auth?response_type=code&scope=signature&client_id=7b22cb84-xxxx-xxxx-xxxx-6bfa579058ea&redirect_uri=https://mozilla.org
Press Enter to navigate to the URL.
Log in to your Docusign developer account and give consent. After you click Allow Access to give the application permission, you will be redirected to your redirect URI.
In the URI in your browser's address bar, select the value of the code parameter at the end of the URI (everything after the equal sign). Note that the entire code value probably will not fit on the screen, so be sure to scroll all the way to the end of the URI to capture the entire value.
Note: After the URI loads in your browser, you have only 120 seconds (2 minutes) to complete the next task in the activity before the code expires.
Acquire Tokens
In Postman, open the collection for a Docusign API, then open the Authentication section.
Open the 01 Authorize Code Grant Access Token request, then select the Body tab.
Replace the placeholder value for the code parameter {{codeFromUrl}} with the value you copied from the URI.
Click Send to send the request.
Verify that your response includes access_token, token_type, refresh_token, expires_in, and scope values.
Note: Docusign REST API Postman collections include post-request scripts that automatically update environment variables in Postman based on response data. As a result, tokens are stored in your Postman environment for you, and your subsequent Authorization Code Grant calls will work without requiring you to perform any additional configuration.
Acquire User Information
Within the Authentication section of the Postman collection, open the 04 Get User Info request.
Select the Headers tab. The request includes the Authorization header with a value of Bearer followed by the environment variable that stores your access token.
Click Send to send the request.
Your response includes account_id and base_uri values within each object in the accounts array.
Now that you have acquired an access token and user information, you have everything you need to make authenticated calls to Docusign APIs within the scopes you specified in your initial authorization code request.
Refresh Tokens
Within the Authentication section of the Postman collection, open the 03 Refresh Access Token request.
Select the Headers tab. The request includes the Authorization header with a value of Basic followed by the environment variable that stores your encoded keys.
Select the Body tab. The request includes the refresh_token key with a value equal to the environment variable that stores your refresh token. It also includes a grant_type key with a string value of refresh_token.
Click Send to send the request.
Your response includes new access_token and refresh_token values.
Lesson 4 - JSON Web Token (JWT) Grant

Implement Authentication for Docusign APIs
Introduction to Docusign API Authentication
AUTHORIZATION CODE GRANT
Confidential and Public Authorization Code Grants
Hands-on Practice
JWT GRANT
JSON Web Token (JWT) Grant
Hands-on Practice
Knowledge Check
Docusign API Authentication Scenarios
Confidential and Public Authorization Code Grants
Objective: After reviewing this topic, you will be able to implement the Docusign Confidential Authorization Code Grant and Public Authorization Code Grant authentication flows.
Authorization Code Grant (Auth Code Grant) is an OAuth 2.0 authentication flow that Docusign APIs support to verify your application's identity and confirm its authorization to act on behalf of a specific user. This flow is ideal for web applications where a user interacts with the application and authenticates using their individual Docusign login.
Docusign offers two versions of auth code grant:
1
Confidential Auth Code Grant: Recommended for server-hosted applications that can securely store a secret key.
2
Public Auth Code Grant: Recommended for single-page applications (SPAs) and native apps that cannot securely store a secret key. This grant flow uses Proof Key for Code Exchange (PKCE) for security.
Both flows require an integration key and a redirect URI configured in eSignature Admin.
Configure Authentication Settings
Before building your authentication flow, you must specify the type of Auth Code Grant your app will use in Docusign Admin:
From your Docusign account, click the Admin tab.
Select Apps and Keys.
If you are starting a new app, click Add App and Integration Key.
OR
If you have already started building your app, select the Actions menu for the app you want to configure, then select Edit.
The app settings page enables you to specify the auth type for your app.
•
For Confidential Auth Code Grant, indicate that your app can securely store a client secret. This is the default setting. You will add a secret key in your app's authentication settings.
•
For Public Auth Code Grant, indicate that your app cannot securely store a client secret and specify whether it's a single-page web application or a native OS application. These settings enable Authorization Code Grant with PKCE.
The Auth Code Grant flow involves three main steps, which must be completed in a specific order, followed by an optional step for token renewal:
Acquire an Authorization Code
Acquire Tokens (Access Token and Refresh Token)
Acquire User Information
Refresh Tokens
Step 1: Acquire an Authorization Code
In this step, your application navigates to a URI to request an authorization code using query string parameters.
Users are prompted to log in and allow access. By doing so, they give permission for Docusign services to authenticate and grant access on their behalf.
This avoids requiring users to approve access to a system every time authorization code or token requests are made in the future.
Base URI
Docusign development and production endpoints use different domains. As a result, the base URI for Docusign authentication varies depending on whether your app is in development or is deployed to production:
Development
https://account-d.docusign.com/oauth/auth
Production
https://account.docusign.com/oauth/auth
Note: All examples in this course use development endpoints. When deploying your app to production, ensure that you update all instances of the URI to use production endpoints.
Required Query String Parameters
Redirect the user's browser to a constructed Docusign authentication URI.
Your HTTP request to the URI must include the following four query string parameters:
•
client_id: Your application's integration key.
•
redirect_uri: The URI where Docusign will redirect the user after consent is given, delivering the authorization code. This must be pre-configured with your integration key.
•
scope: One or more scopes necessary for the API actions your integration will perform, such as signature for most eSignature API actions. The extended scope enables a long refresh token lifecycle.
•
response_type: The value code.
Optional Query String Parameters
Both Auth Code Grant flows also support two optional query parameters:
•
code_challenge and code_challenge_method: For all Public Auth Code Grant implementations, as well as Confidential Auth Code Grant implementations that use PKCE, these parameters verify that the app that starts the flow is the one that finishes it.
To create the value of the code_challenge parameter, your app must generate a cryptographically random string, hash that string with the S256 algorithm, then base64 URL-encode it.
The value of the code_challenge_method parameter is always S256.
These parameters are required when you use the Public Auth Code Grant flow
•
state: Include a state parameter with a random string to prevent Cross-Site Request Forgery (CSRF) attacks.
Response
After the user logs in and grants consent, Docusign redirects back to your redirect_uri, including a code query string parameter containing the authorization code.
https://example.com?code=eyJ0eXAiOiJNVCIs...
Note: This authorization code is only valid for 120 seconds (2 minutes). You must use it in the next step within this timeframe, or it will expire. If your authorization code expires, resubmit the consent url to regenerate the code.
Step 2: Acquire Tokens
Once you have the authorization code, your application can programmatically request access and refresh tokens without further user interaction.
Method and endpoint
POST /oauth/token
Header
For a Confidential Auth Code Grant request, you must base64-encode your integration key followed by a comma and your secret key. You then pass this value in a header with the following syntax:
Authorization: Basic {{encodedKeys}}
To generate the encoded value, you base64-encode a string that consists of your integration key followed by a colon and then your secret key, with no spaces:
integrationKey:secretKey
For example, the following JavaScript code generates a base64 encoded value based on placeholder integration and secret keys:
Note: The header containing encoded keys is required only for Confidential Auth Code Grant. For a Public Auth Code Grant implementation, you instead provide a code_verifier value in the body.
•
code: The authorization code obtained in Step 1.
•
grant_type: authorization_code.
•
client_id: Your application's integration key.
•
code_verifier: The random string you generated to create the code_challenge value when you acquired an authorization code. (Required only for Public Auth Code Grant.)
Required Body Parameters
The following snippet shows a raw HTTP request for tokens to the Docusign authentication service for a Confidential Auth Code Grant implementation:
Response
The response provides an access token (valid for 8 hours) and a refresh token. The refresh token is valid for up to 30 days for Confidential Auth Code Grant and 24 hours for Public Auth Code Grant.
Step 3: Acquire User Information
After obtaining tokens, you need to retrieve specific user account information necessary for making Docusign API calls. This step is crucial because Docusign API request URIs include the user's account ID and base URI.
Method and endpoint
GET /oauth/userinfo
Required Header
Authorization: Bearer {{accessToken}}
Response
The response contains an accounts array. You'll typically use the account with is_default set to true. From the selected account object, extract the account_id and base_uri values, which are essential for constructing all subsequent Docusign API requests.
Step 4: Refresh Tokens
Access tokens expire after 8 hours, but your integration can use a refresh token to obtain a new access token. This enables you to extend application access without requiring users to log in repeatedly.
Method and endpoint
POST /oauth/token
Required Header
Authorization: Basic {{encodedKeys}}
Note: The header containing encoded keys is required only for Confidential Auth Code Grant. For a Public Auth Code Grant implementation, you instead provide a code_verifier value in the body.
Required Body Parameters
•
grant_type: refresh_token
•
client_id: Your application's integration key.
•
refresh_token: The refresh token obtained in Step 2.
•
code_verifier: The random string you generated to create the code_challenge value when you acquired an authorization code. (Required only for Public Auth Code Grant.)
Response
You will receive a new access token and a new refresh token. The previous access token is no longer valid.
The snippet below shows a raw HTTP request to refresh tokens to the Docusign authentication service for a Confidential Auth Code Grant implementation:
Refresh Token Lifecycles
•
With basic permission scopes (e.g., signature only), the refresh token expires 30 days from its original issue date.
•
With the extended scope, the refresh token expires 30 days from the last successful refresh date, allowing for continuous access.
Best Practice
Evaluate your application's security posture before implementing the extended scope due to the longer token validity periods.
Hands-on Practice
Let's walk through the entire Confidential Authorization Code Grant process.
This activity can be completed in 10 minutes.
Setup
To complete this activity, you need a Docusign developer account. If you don't already have one, you can create a developer account
on the Docusign Developer Center.
In your browser, log in to your Docusign developer account.
From the Admin page, click Apps and Keys, then click Add App and Integration Key to create a new app.
Provide a name for your app and click Create App.
Select an Integration Type for your app.
Note: To learn more about the different integration types, explore the Docusign Go-live
process on the Docusign Developer Center.
Click Add Secret Key to create a secret key, copy the value, then save it in secure storage, such as a password/credential manager application.
Click Add URI, then enter https://mozilla.org
or another website of your choice.
Click Save.
Open the Using the Docusign API Postman collections
page on the Docusign Developer Center and follow the steps to set up your environment and fork or import the Postman collection for at least one Docusign API.
In the Environments list, set Docusign-account-d as the active environment.
Acquire an Authorization Code
Copy the following URL to your web browser's address bar:
https://account-d.docusign.com/oauth/auth?response_type=code&scope=signature&client_id={{integrationKey}}&redirect_uri=https://mozilla.org
Replace {{integrationKey}} with your application's integration key, and if necessary replace https://mozilla.org with the redirect URI that you configured for your app in eSignature Admin.
https://account-d.docusign.com/oauth/auth?response_type=code&scope=signature&client_id=7b22cb84-xxxx-xxxx-xxxx-6bfa579058ea&redirect_uri=https://mozilla.org
Press Enter to navigate to the URL.
Log in to your Docusign developer account and give consent. After you click Allow Access to give the application permission, you will be redirected to your redirect URI.
In the URI in your browser's address bar, select the value of the code parameter at the end of the URI (everything after the equal sign). Note that the entire code value probably will not fit on the screen, so be sure to scroll all the way to the end of the URI to capture the entire value.
Note: After the URI loads in your browser, you have only 120 seconds (2 minutes) to complete the next task in the activity before the code expires.
Acquire Tokens
In Postman, open the collection for a Docusign API, then open the Authentication section.
Open the 01 Authorize Code Grant Access Token request, then select the Body tab.
Replace the placeholder value for the code parameter {{codeFromUrl}} with the value you copied from the URI.
Click Send to send the request.
Verify that your response includes access_token, token_type, refresh_token, expires_in, and scope values.
Note: Docusign REST API Postman collections include post-request scripts that automatically update environment variables in Postman based on response data. As a result, tokens are stored in your Postman environment for you, and your subsequent Authorization Code Grant calls will work without requiring you to perform any additional configuration.
Acquire User Information
Within the Authentication section of the Postman collection, open the 04 Get User Info request.
Select the Headers tab. The request includes the Authorization header with a value of Bearer followed by the environment variable that stores your access token.
Click Send to send the request.
Your response includes account_id and base_uri values within each object in the accounts array.
Now that you have acquired an access token and user information, you have everything you need to make authenticated calls to Docusign APIs within the scopes you specified in your initial authorization code request.
Refresh Tokens
Within the Authentication section of the Postman collection, open the 03 Refresh Access Token request.
Select the Headers tab. The request includes the Authorization header with a value of Basic followed by the environment variable that stores your encoded keys.
Select the Body tab. The request includes the refresh_token key with a value equal to the environment variable that stores your refresh token. It also includes a grant_type key with a string value of refresh_token.
Click Send to send the request.
Your response includes new access_token and refresh_token values.
Lesson 3 - Hands-on Practice

### Create Custom Docusign Connect Webhooks 30 min

Create Custom Docusign Connect Webhooks
Custom Connect Overview
Custom Connect Configuration Levels and Options
CREATE CUSTOM CONNECT CONFIGURATIONS
Configure Organization-Level and Account-Level Webhooks
Configure Envelope-Level Webhooks
Manage Webhooks for an Organization
Activity: Create a Custom Connect Configuration
Custom Connect Overview
Build more efficient workflows, simplify your logic, and avoid hitting polling limits.
Docusign Connect
sends real-time messages about Docusign account activity to another application. You choose the Docusign account events you want to follow.
When an event that you follow happens, Connect sends an event message to the listening application in JSON or XML format. For example, you can receive updates when an envelope is resent or corrected, a recipient reassigns an envelope, or a template is created. Your application can then process the notification message as needed.
Developers can create several types of custom Connect configurations:
An organization-level Connect configuration sends updates for trigger events on envelopes sent from or received by your Docusign organization.
An account-level Connect configuration sends updates for trigger events on envelopes sent from or received by your Docusign account.
An envelope-level Sender Connect configuration sends updates for trigger events on a specific envelope sent by your Docusign account.
Note: A Docusign account can be used to organize multiple users into a functional group. A Docusign organization enables you to administer settings in a single location for multiple accounts. To learn more about Docusign organizations, review Introduction to Docusign Organization Administration
on the Docusign Support Center.
All three custom Connect types can be configured to send updates in response to several different envelope events and recipient actions.
Article: Docusign Connect overview (webhooks)
This article describes how Docusign Connect works and considerations for using it, including when to use it, Connect security, and events that can trigger Connect.
CONNECT OVERVIEW
Why Not Use Polling?
The Docusign eSignature REST API limits GET requests to one per envelope every 15 minutes. You can avoid making unnecessary API calls that would count against your limit by using Connect webhooks to configure push notifications instead. Connect offers the following advantages over polling:
The returned information does not count against your API request limits because Docusign is sending it directly to you.
Messages are delivered to your listener only when an envelope changes; in other words, only when you need to take action of some sort.
You avoid custom and cumbersome polling logic within your application that would have to manage the data returned and when to query again.
Choosing a Docusign Connect Solution
In addition to custom configurations, account-level Connect also supports pre-built solutions for popular third-party services.
Pre-built solutions can be useful when you need to archive completed documents with a popular third-party service.
Custom Connect configurations may be the best choice if you need to integrate with an internal system for storage or to initiate additional steps after an envelope status changes.
Using Docusign Connect with a Pre-Built Third-Party Integration
Docusign supports pre-built integrations for Box, OneDrive, Salesforce, and eOriginal. The data that Docusign Connect pushes varies depending on the third-party service:
Connect for Box and Connect for OneDrive push completed documents to a Box or OneDrive folder, respectively.
Connect for Salesforce pushes data updates to the Docusign for Salesforce application.
Connect for eOriginal pushes an event to eOriginal informing the eOriginal system that a transaction that needs to be vaulted is complete.
Using Docusign Connect with a Custom Configuration
Creating a custom configuration to send events to your custom listener enables you to:
Store signed documents in an organization's custom storage system.
Trigger additional business actions after an envelope has been completed. For example, initiate automatic provisioning or shipment after a contract has been signed.
Automatically update business data systems with data from a signed envelope. For example, if a signer updated their address as part of the signing process, you could start the process to update the signer's address in line-of-business applications.
Lesson 2 - Custom Connect Configuration Levels and Options

Create Custom Docusign Connect Webhooks
Welcome to the Create Custom Docusign Connect Webhooks course. After reviewing this course, you will be able to:
Explain the differences between organization-level, account-level, and envelope-level webhooks.
Create custom organization-level, account-level, and envelope-level Connect configurations.
Manage Connect webhooks across an organization.
Describe best practices for building a Docusign Connect integration.
Custom Connect Overview
Custom Connect Configuration Levels and Options
CREATE CUSTOM CONNECT CONFIGURATIONS
Configure Organization-Level and Account-Level Webhooks
Configure Envelope-Level Webhooks
Manage Webhooks for an Organization
Activity: Create a Custom Connect Configuration

Create Custom Docusign Connect Webhooks
Custom Connect Overview
Custom Connect Configuration Levels and Options
CREATE CUSTOM CONNECT CONFIGURATIONS
Configure Organization-Level and Account-Level Webhooks
Configure Envelope-Level Webhooks
Manage Webhooks for an Organization
Activity: Create a Custom Connect Configuration
Custom Connect Configuration Levels and Options
Objective: After reviewing this topic, you will be able to describe the configuration levels and options for setting up custom Docusign Connect webhooks.
Docusign Connect supports multiple levels of custom configurations. Connect also offers options for the data and frequency of message.
Connect Configuration Levels
Docusign Connect supports custom configurations at three levels:
Organization-level Connect
Account-level Connect
Envelope-level Connect
Each option serves a specific use case. You can implement one, two, or all of these levels to meet your webhook needs.
Organization-Level Connect
An organization-level Connect webhook generates notifications about envelopes sent from or received by your organization that meet your selection criteria. You can set organization-level Connect webhooks to listen for events for envelopes sent or received by all accounts or by selected accounts within your organization. These events are tracked, and can be delivered to a listening application.
Docousign Organization Admin page
An organization-level webhook can be set up in two ways: through the Docusign Organization Admin page or via the API.
Account-Level Connect
An account-level Connect webhook generates notifications about envelopes sent from or received by your account that meet your selection criteria. You can set account-level Connect webhooks to listen for events for envelopes sent or received by all users or by selected users on your account. These events are tracked, and can be delivered to a listening application.
Docusign eSignature Admin page
An account-level webhook can be set up in two ways: through the Docusign eSignature Admin page or via the API.
Envelope-Level Connect
An envelope-level Connect webhook is configured by applying an eventNotification property to an envelope when you create or send it through the API. This eventNotification property must be set through the API; you cannot create an envelope-level webhook using the eSignature Send page. You create an envelope-level webhook using the Envelopes: create method.
Because envelope-level webhooks can be configured only when an envelope is sent, envelope-level webhooks are not available for envelopes received by your account members from external parties.
Key Differences Among Configuration Levels
Organization-Level Connect Webhooks
Account-Level Connect Webhooks
Envelope-Level Connect Webhooks
Used for all envelopes sent from or received by any account or user within an organization
Used for all envelopes sent from or received by an account and any user within the account
Used for a specific envelope sent via the API
Configured using the Docusign Organization Admin page or using the API
Configured using the eSignature Admin page or using the API
Configured using the API only, through the eventNotification object
Available on select Docusign plans
Available on all plans with API access
Configured once, then used until disabled
Configured per envelope - must be reconfigured on next envelope
Default Message Data Format
The Connect settings that Docusign recommends send individual messages in JSON format. You may see this option referred to as JSON Send Individual Messages format, JSON SIM format, or Connect 2.0.
Unlike messages in the previous supported formats, the JSON SIM message format is event-focused rather than envelope-focused. This means that:
By default, rather than getting a summary of the envelope in each message, the message contains data about the triggering event. This means that each message is much smaller, more focused on the data you request, more customizable, and easier to process. Depending on the event type, you may choose to include the envelope summary as well.
You can track and subscribe to more types of events.
You receive an event notification status at the time it occurs.
Because the JSON SIM format provides substantial benefits over other message formats such as XML SIM or aggregate, it is recommended for all apps.
The JSON SIM format is supported for organization-level, account-level, and envelope-level Connect.
Legacy Configuration Options
Custom Connect configurations support legacy options to send messages in XML format rather than JSON, and to aggregate some messages together.
Note: Legacy configurations are available only for account-level and envelope-level configurations. All organization-level configurations use the JSON SIM model.
XML Data Format
The legacy data format is XML-based, and you can configure event messages as SOAP requests. The format uses the same object model as the Docusign eSignature SOAP API.
You may want to consider the legacy format if any of the following apply to you:
Prefer XML
Prefer to standardize parsers and object models against the SOAP API
Want to use the SOAP interface
Want to ensure payload never changes over the course of your integration
Message Aggregation
By default, new Connect configurations use SIM mode, which sends a message for each event triggered. SIM provides a fine-grained integration between Docusign and your external systems, and Docusign recommends it for new Connect configurations.
In a Connect configuration that uses the XML data type, you can instead choose the aggregate option to combine similar events into a single message delivery. This option can reduce the overall number of messages that your listener receives. For example, when an envelope is signed by the final recipient, this triggers two events: recipient complete and envelope complete. Instead of sending each of these messages separately, the aggregated messages model combines them and triggers just one Connect event for your webhook listener.
However, if you are concerned only with the overall lifecycle and don't need as much granular control, aggregate mode may be appropriate for your configuration.
Activity: Create a Custom Connect Configuration
Objective: After reviewing this topic, you will be able to set up a webhook listener, create a Connect configuration, and receive a Connect message.
Complete the following steps to create and test an account-level Connect configuration.
This activity should take about 15 minutes to complete.
Setup
Before beginning this activity, be sure you have a Docusign developer account. You can create a free developer account
at the Docusign Developer Center.
Configure the Postman Collection and Environment
1
Download the following Postman collection and Postman environment files:
Connect Webhooks.postman_collection.json
3.7 KB
Connect Webhooks.postman_environment.json
549 B
2
In Postman, create a new workspace, then import both the collection and environment files you downloaded.
3
In the Postman sidebar, click Environments, click the Connect Webhooks environment to open it, then set it as the active environment.
4
Navigate to the following URL to open the Apps and Keys page for your Docusign Developer account: https://apps-d.docusign.com/admin/apps-and-keys
5
Copy the API Account Id value from your Apps and Keys page, then in Postman paste it as the current value for the accountId environment variable.
6
Create a new Docusign Integration Key or open an existing one for editing.
7
On the app settings page, in the Integration Type section, choose a classification for your app.
Note: To learn more about the different classifications, explore the Docusign Go-live
process on the Docusign Developer Center.
7
Copy the Integration Key value and paste it as the current value of the iKey variable in Postman, create a Secret Key and paste it as the current value of the iSec variable in Postman, then save your changes to the Postman environment.
8
On the Docusign app settings page, add a Redirect URI with the value https://oauth.pstmn.io/v1/browser-callback and click Save.
9
In the Postman sidebar, click Collections, click Connect Webhooks, then click the Authorization or Auth tab.
10
Click the Get New Access Token button, click the Allow Access button to grant the Postman collection permission to connect to your Docusign app, then click Use Token.
Configure a Webhook Listener
1
Open an online webhook service such as https://webhook.site
and if necessary, sign up for an account.
2
Create a new webhook and specify 200 OK for the response status.
3
Copy the generated URL for your webhook to the clipboard for use in the next set of steps.
Create a Connect Configuration
1
In Postman, within the Connect Webhooks folder, open the Create a Connect Configuration request.
2
On the Body tab, replace the value of the urlToPublishTo property with the URL of the webhook you created in the previous steps, then change the value of the allowEnvelopePublish property to true.
3
Examine the specified values for the events property as well as the other property values, then save your changes to the Postman request.
4
Click Send and then inspect the response.
A successful response includes a unique value for the connectId property, as well as values for all the Connect configuration options you specified in your request and default values for any unspecified properties.
Send an Envelope and View a Connect Message
1
In the Docusign eSignature app, click the Home tab, then create and send an envelope.
2
Return to the web page for your webhook listener, then examine the details for the Connect message that your listener has received.
3
Examine the content of the data included in the Connect message body.
Lesson 3 - Configure Organization-Level and Account-Level Webhooks

Create Custom Docusign Connect Webhooks
Custom Connect Overview
Custom Connect Configuration Levels and Options
CREATE CUSTOM CONNECT CONFIGURATIONS
Configure Organization-Level and Account-Level Webhooks
Configure Envelope-Level Webhooks
Manage Webhooks for an Organization
Activity: Create a Custom Connect Configuration
Lesson 1 - Custom Connect Overview
Custom Connect Configuration Levels and Options
Objective: After reviewing this topic, you will be able to describe the configuration levels and options for setting up custom Docusign Connect webhooks.
Docusign Connect supports multiple levels of custom configurations. Connect also offers options for the data and frequency of message.
Connect Configuration Levels
Docusign Connect supports custom configurations at three levels:
Organization-level Connect
Account-level Connect
Envelope-level Connect
Each option serves a specific use case. You can implement one, two, or all of these levels to meet your webhook needs.
Organization-Level Connect
An organization-level Connect webhook generates notifications about envelopes sent from or received by your organization that meet your selection criteria. You can set organization-level Connect webhooks to listen for events for envelopes sent or received by all accounts or by selected accounts within your organization. These events are tracked, and can be delivered to a listening application.
Docousign Organization Admin page
An organization-level webhook can be set up in two ways: through the Docusign Organization Admin page or via the API.
Account-Level Connect
An account-level Connect webhook generates notifications about envelopes sent from or received by your account that meet your selection criteria. You can set account-level Connect webhooks to listen for events for envelopes sent or received by all users or by selected users on your account. These events are tracked, and can be delivered to a listening application.
Docusign eSignature Admin page
An account-level webhook can be set up in two ways: through the Docusign eSignature Admin page or via the API.
Envelope-Level Connect
An envelope-level Connect webhook is configured by applying an eventNotification property to an envelope when you create or send it through the API. This eventNotification property must be set through the API; you cannot create an envelope-level webhook using the eSignature Send page. You create an envelope-level webhook using the Envelopes: create method.
Because envelope-level webhooks can be configured only when an envelope is sent, envelope-level webhooks are not available for envelopes received by your account members from external parties.
Key Differences Among Configuration Levels
Organization-Level Connect Webhooks
Account-Level Connect Webhooks
Envelope-Level Connect Webhooks
Used for all envelopes sent from or received by any account or user within an organization
Used for all envelopes sent from or received by an account and any user within the account
Used for a specific envelope sent via the API
Configured using the Docusign Organization Admin page or using the API
Configured using the eSignature Admin page or using the API
Configured using the API only, through the eventNotification object
Available on select Docusign plans
Available on all plans with API access
Configured once, then used until disabled
Configured per envelope - must be reconfigured on next envelope
Default Message Data Format
The Connect settings that Docusign recommends send individual messages in JSON format. You may see this option referred to as JSON Send Individual Messages format, JSON SIM format, or Connect 2.0.
Unlike messages in the previous supported formats, the JSON SIM message format is event-focused rather than envelope-focused. This means that:
By default, rather than getting a summary of the envelope in each message, the message contains data about the triggering event. This means that each message is much smaller, more focused on the data you request, more customizable, and easier to process. Depending on the event type, you may choose to include the envelope summary as well.
You can track and subscribe to more types of events.
You receive an event notification status at the time it occurs.
Because the JSON SIM format provides substantial benefits over other message formats such as XML SIM or aggregate, it is recommended for all apps.
The JSON SIM format is supported for organization-level, account-level, and envelope-level Connect.
Legacy Configuration Options
Custom Connect configurations support legacy options to send messages in XML format rather than JSON, and to aggregate some messages together.
Note: Legacy configurations are available only for account-level and envelope-level configurations. All organization-level configurations use the JSON SIM model.
XML Data Format
The legacy data format is XML-based, and you can configure event messages as SOAP requests. The format uses the same object model as the Docusign eSignature SOAP API.
You may want to consider the legacy format if any of the following apply to you:
Prefer XML
Prefer to standardize parsers and object models against the SOAP API
Want to use the SOAP interface
Want to ensure payload never changes over the course of your integration
Message Aggregation
By default, new Connect configurations use SIM mode, which sends a message for each event triggered. SIM provides a fine-grained integration between Docusign and your external systems, and Docusign recommends it for new Connect configurations.
In a Connect configuration that uses the XML data type, you can instead choose the aggregate option to combine similar events into a single message delivery. This option can reduce the overall number of messages that your listener receives. For example, when an envelope is signed by the final recipient, this triggers two events: recipient complete and envelope complete. Instead of sending each of these messages separately, the aggregated messages model combines them and triggers just one Connect event for your webhook listener.
However, if you are concerned only with the overall lifecycle and don't need as much granular control, aggregate mode may be appropriate for your configuration.
Lesson 3 - Configure Organization-Level and Account-Level Webhooks

Create Custom Docusign Connect Webhooks
Custom Connect Overview
Custom Connect Configuration Levels and Options
CREATE CUSTOM CONNECT CONFIGURATIONS
Configure Organization-Level and Account-Level Webhooks
Configure Envelope-Level Webhooks
Manage Webhooks for an Organization
Activity: Create a Custom Connect Configuration
Custom Connect Overview
Build more efficient workflows, simplify your logic, and avoid hitting polling limits.
Docusign Connect
sends real-time messages about Docusign account activity to another application. You choose the Docusign account events you want to follow.
When an event that you follow happens, Connect sends an event message to the listening application in JSON or XML format. For example, you can receive updates when an envelope is resent or corrected, a recipient reassigns an envelope, or a template is created. Your application can then process the notification message as needed.
Developers can create several types of custom Connect configurations:
An organization-level Connect configuration sends updates for trigger events on envelopes sent from or received by your Docusign organization.
An account-level Connect configuration sends updates for trigger events on envelopes sent from or received by your Docusign account.
An envelope-level Sender Connect configuration sends updates for trigger events on a specific envelope sent by your Docusign account.
Note: A Docusign account can be used to organize multiple users into a functional group. A Docusign organization enables you to administer settings in a single location for multiple accounts. To learn more about Docusign organizations, review Introduction to Docusign Organization Administration
on the Docusign Support Center.
All three custom Connect types can be configured to send updates in response to several different envelope events and recipient actions.
Article: Docusign Connect overview (webhooks)
This article describes how Docusign Connect works and considerations for using it, including when to use it, Connect security, and events that can trigger Connect.
CONNECT OVERVIEW
Why Not Use Polling?
The Docusign eSignature REST API limits GET requests to one per envelope every 15 minutes. You can avoid making unnecessary API calls that would count against your limit by using Connect webhooks to configure push notifications instead. Connect offers the following advantages over polling:
The returned information does not count against your API request limits because Docusign is sending it directly to you.
Messages are delivered to your listener only when an envelope changes; in other words, only when you need to take action of some sort.
You avoid custom and cumbersome polling logic within your application that would have to manage the data returned and when to query again.
Choosing a Docusign Connect Solution
In addition to custom configurations, account-level Connect also supports pre-built solutions for popular third-party services.
Pre-built solutions can be useful when you need to archive completed documents with a popular third-party service.
Custom Connect configurations may be the best choice if you need to integrate with an internal system for storage or to initiate additional steps after an envelope status changes.
Using Docusign Connect with a Pre-Built Third-Party Integration
Docusign supports pre-built integrations for Box, OneDrive, Salesforce, and eOriginal. The data that Docusign Connect pushes varies depending on the third-party service:
Connect for Box and Connect for OneDrive push completed documents to a Box or OneDrive folder, respectively.
Connect for Salesforce pushes data updates to the Docusign for Salesforce application.
Connect for eOriginal pushes an event to eOriginal informing the eOriginal system that a transaction that needs to be vaulted is complete.
Using Docusign Connect with a Custom Configuration
Creating a custom configuration to send events to your custom listener enables you to:
Store signed documents in an organization's custom storage system.
Trigger additional business actions after an envelope has been completed. For example, initiate automatic provisioning or shipment after a contract has been signed.
Automatically update business data systems with data from a signed envelope. For example, if a signer updated their address as part of the signing process, you could start the process to update the signer's address in line-of-business applications.
Custom Connect Configuration Levels and Options
Objective: After reviewing this topic, you will be able to describe the configuration levels and options for setting up custom Docusign Connect webhooks.
Docusign Connect supports multiple levels of custom configurations. Connect also offers options for the data and frequency of message.
Connect Configuration Levels
Docusign Connect supports custom configurations at three levels:
Organization-level Connect
Account-level Connect
Envelope-level Connect
Each option serves a specific use case. You can implement one, two, or all of these levels to meet your webhook needs.
Organization-Level Connect
An organization-level Connect webhook generates notifications about envelopes sent from or received by your organization that meet your selection criteria. You can set organization-level Connect webhooks to listen for events for envelopes sent or received by all accounts or by selected accounts within your organization. These events are tracked, and can be delivered to a listening application.
Docousign Organization Admin page
An organization-level webhook can be set up in two ways: through the Docusign Organization Admin page or via the API.
Account-Level Connect
An account-level Connect webhook generates notifications about envelopes sent from or received by your account that meet your selection criteria. You can set account-level Connect webhooks to listen for events for envelopes sent or received by all users or by selected users on your account. These events are tracked, and can be delivered to a listening application.
Docusign eSignature Admin page
An account-level webhook can be set up in two ways: through the Docusign eSignature Admin page or via the API.
Envelope-Level Connect
An envelope-level Connect webhook is configured by applying an eventNotification property to an envelope when you create or send it through the API. This eventNotification property must be set through the API; you cannot create an envelope-level webhook using the eSignature Send page. You create an envelope-level webhook using the Envelopes: create method.
Because envelope-level webhooks can be configured only when an envelope is sent, envelope-level webhooks are not available for envelopes received by your account members from external parties.
Key Differences Among Configuration Levels
Organization-Level Connect Webhooks
Account-Level Connect Webhooks
Envelope-Level Connect Webhooks
Used for all envelopes sent from or received by any account or user within an organization
Used for all envelopes sent from or received by an account and any user within the account
Used for a specific envelope sent via the API
Configured using the Docusign Organization Admin page or using the API
Configured using the eSignature Admin page or using the API
Configured using the API only, through the eventNotification object
Available on select Docusign plans
Available on all plans with API access
Configured once, then used until disabled
Configured per envelope - must be reconfigured on next envelope
Default Message Data Format
The Connect settings that Docusign recommends send individual messages in JSON format. You may see this option referred to as JSON Send Individual Messages format, JSON SIM format, or Connect 2.0.
Unlike messages in the previous supported formats, the JSON SIM message format is event-focused rather than envelope-focused. This means that:
By default, rather than getting a summary of the envelope in each message, the message contains data about the triggering event. This means that each message is much smaller, more focused on the data you request, more customizable, and easier to process. Depending on the event type, you may choose to include the envelope summary as well.
You can track and subscribe to more types of events.
You receive an event notification status at the time it occurs.
Because the JSON SIM format provides substantial benefits over other message formats such as XML SIM or aggregate, it is recommended for all apps.
The JSON SIM format is supported for organization-level, account-level, and envelope-level Connect.
Legacy Configuration Options
Custom Connect configurations support legacy options to send messages in XML format rather than JSON, and to aggregate some messages together.
Note: Legacy configurations are available only for account-level and envelope-level configurations. All organization-level configurations use the JSON SIM model.
XML Data Format
The legacy data format is XML-based, and you can configure event messages as SOAP requests. The format uses the same object model as the Docusign eSignature SOAP API.
You may want to consider the legacy format if any of the following apply to you:
Prefer XML
Prefer to standardize parsers and object models against the SOAP API
Want to use the SOAP interface
Want to ensure payload never changes over the course of your integration
Message Aggregation
By default, new Connect configurations use SIM mode, which sends a message for each event triggered. SIM provides a fine-grained integration between Docusign and your external systems, and Docusign recommends it for new Connect configurations.
In a Connect configuration that uses the XML data type, you can instead choose the aggregate option to combine similar events into a single message delivery. This option can reduce the overall number of messages that your listener receives. For example, when an envelope is signed by the final recipient, this triggers two events: recipient complete and envelope complete. Instead of sending each of these messages separately, the aggregated messages model combines them and triggers just one Connect event for your webhook listener.
However, if you are concerned only with the overall lifecycle and don't need as much granular control, aggregate mode may be appropriate for your configuration.
Lesson 2 - Custom Connect Configuration Levels and Options

Create Custom Docusign Connect Webhooks
Custom Connect Overview
Custom Connect Configuration Levels and Options
CREATE CUSTOM CONNECT CONFIGURATIONS
Configure Organization-Level and Account-Level Webhooks
Configure Envelope-Level Webhooks
Manage Webhooks for an Organization
Activity: Create a Custom Connect Configuration
Custom Connect Configuration Levels and Options
Objective: After reviewing this topic, you will be able to describe the configuration levels and options for setting up custom Docusign Connect webhooks.
Docusign Connect supports multiple levels of custom configurations. Connect also offers options for the data and frequency of message.
Connect Configuration Levels
Docusign Connect supports custom configurations at three levels:
Organization-level Connect
Account-level Connect
Envelope-level Connect
Each option serves a specific use case. You can implement one, two, or all of these levels to meet your webhook needs.
Organization-Level Connect
An organization-level Connect webhook generates notifications about envelopes sent from or received by your organization that meet your selection criteria. You can set organization-level Connect webhooks to listen for events for envelopes sent or received by all accounts or by selected accounts within your organization. These events are tracked, and can be delivered to a listening application.
Docousign Organization Admin page
An organization-level webhook can be set up in two ways: through the Docusign Organization Admin page or via the API.
Account-Level Connect
An account-level Connect webhook generates notifications about envelopes sent from or received by your account that meet your selection criteria. You can set account-level Connect webhooks to listen for events for envelopes sent or received by all users or by selected users on your account. These events are tracked, and can be delivered to a listening application.
Docusign eSignature Admin page
An account-level webhook can be set up in two ways: through the Docusign eSignature Admin page or via the API.
Envelope-Level Connect
An envelope-level Connect webhook is configured by applying an eventNotification property to an envelope when you create or send it through the API. This eventNotification property must be set through the API; you cannot create an envelope-level webhook using the eSignature Send page. You create an envelope-level webhook using the Envelopes: create method.
Because envelope-level webhooks can be configured only when an envelope is sent, envelope-level webhooks are not available for envelopes received by your account members from external parties.
Key Differences Among Configuration Levels
Organization-Level Connect Webhooks
Account-Level Connect Webhooks
Envelope-Level Connect Webhooks
Used for all envelopes sent from or received by any account or user within an organization
Used for all envelopes sent from or received by an account and any user within the account
Used for a specific envelope sent via the API
Configured using the Docusign Organization Admin page or using the API
Configured using the eSignature Admin page or using the API
Configured using the API only, through the eventNotification object
Available on select Docusign plans
Available on all plans with API access
Configured once, then used until disabled
Configured per envelope - must be reconfigured on next envelope
Default Message Data Format
The Connect settings that Docusign recommends send individual messages in JSON format. You may see this option referred to as JSON Send Individual Messages format, JSON SIM format, or Connect 2.0.
Unlike messages in the previous supported formats, the JSON SIM message format is event-focused rather than envelope-focused. This means that:
By default, rather than getting a summary of the envelope in each message, the message contains data about the triggering event. This means that each message is much smaller, more focused on the data you request, more customizable, and easier to process. Depending on the event type, you may choose to include the envelope summary as well.
You can track and subscribe to more types of events.
You receive an event notification status at the time it occurs.
Because the JSON SIM format provides substantial benefits over other message formats such as XML SIM or aggregate, it is recommended for all apps.
The JSON SIM format is supported for organization-level, account-level, and envelope-level Connect.
Legacy Configuration Options
Custom Connect configurations support legacy options to send messages in XML format rather than JSON, and to aggregate some messages together.
Note: Legacy configurations are available only for account-level and envelope-level configurations. All organization-level configurations use the JSON SIM model.
XML Data Format
The legacy data format is XML-based, and you can configure event messages as SOAP requests. The format uses the same object model as the Docusign eSignature SOAP API.
You may want to consider the legacy format if any of the following apply to you:
Prefer XML
Prefer to standardize parsers and object models against the SOAP API
Want to use the SOAP interface
Want to ensure payload never changes over the course of your integration
Message Aggregation
By default, new Connect configurations use SIM mode, which sends a message for each event triggered. SIM provides a fine-grained integration between Docusign and your external systems, and Docusign recommends it for new Connect configurations.
In a Connect configuration that uses the XML data type, you can instead choose the aggregate option to combine similar events into a single message delivery. This option can reduce the overall number of messages that your listener receives. For example, when an envelope is signed by the final recipient, this triggers two events: recipient complete and envelope complete. Instead of sending each of these messages separately, the aggregated messages model combines them and triggers just one Connect event for your webhook listener.
However, if you are concerned only with the overall lifecycle and don't need as much granular control, aggregate mode may be appropriate for your configuration.
Custom Connect Overview
Build more efficient workflows, simplify your logic, and avoid hitting polling limits.
Docusign Connect
sends real-time messages about Docusign account activity to another application. You choose the Docusign account events you want to follow.
When an event that you follow happens, Connect sends an event message to the listening application in JSON or XML format. For example, you can receive updates when an envelope is resent or corrected, a recipient reassigns an envelope, or a template is created. Your application can then process the notification message as needed.
Developers can create several types of custom Connect configurations:
An organization-level Connect configuration sends updates for trigger events on envelopes sent from or received by your Docusign organization.
An account-level Connect configuration sends updates for trigger events on envelopes sent from or received by your Docusign account.
An envelope-level Sender Connect configuration sends updates for trigger events on a specific envelope sent by your Docusign account.
Note: A Docusign account can be used to organize multiple users into a functional group. A Docusign organization enables you to administer settings in a single location for multiple accounts. To learn more about Docusign organizations, review Introduction to Docusign Organization Administration
on the Docusign Support Center.
All three custom Connect types can be configured to send updates in response to several different envelope events and recipient actions.
Article: Docusign Connect overview (webhooks)
This article describes how Docusign Connect works and considerations for using it, including when to use it, Connect security, and events that can trigger Connect.
CONNECT OVERVIEW
Why Not Use Polling?
The Docusign eSignature REST API limits GET requests to one per envelope every 15 minutes. You can avoid making unnecessary API calls that would count against your limit by using Connect webhooks to configure push notifications instead. Connect offers the following advantages over polling:
The returned information does not count against your API request limits because Docusign is sending it directly to you.
Messages are delivered to your listener only when an envelope changes; in other words, only when you need to take action of some sort.
You avoid custom and cumbersome polling logic within your application that would have to manage the data returned and when to query again.
Choosing a Docusign Connect Solution
In addition to custom configurations, account-level Connect also supports pre-built solutions for popular third-party services.
Pre-built solutions can be useful when you need to archive completed documents with a popular third-party service.
Custom Connect configurations may be the best choice if you need to integrate with an internal system for storage or to initiate additional steps after an envelope status changes.
Using Docusign Connect with a Pre-Built Third-Party Integration
Docusign supports pre-built integrations for Box, OneDrive, Salesforce, and eOriginal. The data that Docusign Connect pushes varies depending on the third-party service:
Connect for Box and Connect for OneDrive push completed documents to a Box or OneDrive folder, respectively.
Connect for Salesforce pushes data updates to the Docusign for Salesforce application.
Connect for eOriginal pushes an event to eOriginal informing the eOriginal system that a transaction that needs to be vaulted is complete.
Using Docusign Connect with a Custom Configuration
Creating a custom configuration to send events to your custom listener enables you to:
Store signed documents in an organization's custom storage system.
Trigger additional business actions after an envelope has been completed. For example, initiate automatic provisioning or shipment after a contract has been signed.
Automatically update business data systems with data from a signed envelope. For example, if a signer updated their address as part of the signing process, you could start the process to update the signer's address in line-of-business applications.
Lesson 3 - Configure Organization-Level and Account-Level Webhooks

### Go-live with API Integrations 20 min

Go-live with API Integrations
Go-live Process Overview
Go-live with a Custom Integration
Troubleshooting Your Integration
Knowledge Check
Lesson 1 - Go-live Process Overview
Go-live with a Custom Integration
Objective: After reviewing this topic, you will be able to submit a Docusign integration to go-live.
When submitting a go-live request, your integration will go through a validation and approval process, which is required for all Docusign developers (customers and partners). You also must set up a production account that has the proper features enabled for your Docusign integration.
There is no cost associated with submitting an application to go-live, but there might be a charge for Docusign production accounts.
The go-live process involves three main steps:
Create your integration.
Request a production account.
Submit your integration to Go Live
Create Your Integration
To create and configure an integration key in your Docusign developer account, complete the following steps:
1
In your browser, navigate to https://developers.docusign.com
2
Click Developer Account in the top right corner.
•
If you have a developer account, click Log in and follow the prompts to log into your account.
•
If you do not have a developer account, click Create account, then follow the prompts to create an account.
3
Navigate to https://apps-d.docusign.com/admin/apps-and-keys
to open the Apps and Keys page for your developer account.
4
Click Add App and Integration Key.
5
Enter a name for your integration, then click Create App.
6
After the heading How will you use this integration?, select the option that applies to your integration.
Note: You must select an option in the How will you use this integration? section before you can complete the go-live process for your integration.
7
Specify any other settings required for your integration, including authentication, redirect URIs, and CORS configuration, then click Save.
Request a Production Account
A Docusign production account is required in order for any integration to go-live. eSignature transactions captured using a developer account are not legally binding. Once your integration moves from the developer environment to the production environment, the integration's eSignature transactions become legally binding.
Verify API Plans and Feature Availability
Ensure Administrator Privileges
Submit Your Integration to Go Live
When you are ready to go live with your integration, follow these steps:
1
Navigate to https://apps-d.docusign.com/admin/apps-and-keys
to open the Apps and Keys page for your developer account.
2
In the Apps and Integration Keys list, click the Actions menu for your integration, then click Start Go live.
3
In the window that opens, enter the login information for the production account that you want to host the integration after it goes live.
4
Select the production account from the list of accounts displayed, then click Select.
Note: If an error message is displayed instead of a list of accounts, this means the integration type you specified while setting up your integration key does not match the account type you logged into. Follow the troubleshooting steps shown in the error message to resolve this issue, then repeat the previous steps.
5
In the Apps and Integration Keys list, your integration now displays the status of your go-live request:
•
App is live: Your integration key is now available in your production account.
•
Pending approval: Your integration requires a manual approval process, which may take up to 48 hours.
Note: The validation and approval process ensures developers use the proper account type and classify their integration keys accurately. In some cases, this process requires manual review by Docusign teams to verify that security, compliance, and quality standards are met.
The Apps and Integration Keys list displays real-time go-live status for all integrations. When your integration passes review and goes live, you can view it in production. If issues are found, you will be asked to make corrections before proceeding.
Note: The go-live process no longer requires making 20 eSign API calls. This means you can start the submission process immediately after setting up an integration.
Lesson 3 - Troubleshooting Your Integration

Go-live with API Integrations
RESUME COURSE
Welcome to the Go-live with API Integrations course. After reviewing this course, you will be able to move a Docusign integration from a development environment to a production environment using the described processes and best practices.
Go-live Process Overview
Go-live with a Custom Integration
Troubleshooting Your Integration
Knowledge Check

Go-live with API Integrations
Go-live Process Overview
Go-live with a Custom Integration
Troubleshooting Your Integration
Knowledge Check
Congratulations, you have completed this course!
Please provide feedback on this learning experience and content by completing the brief survey below.
Close the Course
EXIT

Go-live with API Integrations
Go-live Process Overview
Go-live with a Custom Integration
Troubleshooting Your Integration
Knowledge Check
Troubleshooting Your Integration
Objective: After reviewing this topic, you will be able to check API logs and monitor application efficiency.
After your integration goes live, Docusign provides several tools to help you troubleshoot issues you may experience:
eSignature Request Logging
eSignature Dashboard
eSignature Usage Center
eSignature Request Logging
The API request logging feature is not enabled by default. You must enable the logs first to get the updates. You can check the API logs via a web application or API logging tool. Docusign recommends checking API logs periodically to ensure the accuracy of your requests and responses. Review the following steps for enabling, viewing or clearing API logs within the Docusign eSignature app.
Note:
Request logging is available to all users, not just developers. Wide availability allows your support staff to debug problems with your user account.
Step 1: Navigate to the account settings
Select the account icon showing your initials at the top right, then select My Preferences.
Step 2: Enable the logging feature
Select Enable Logging to begin logging API requests for your account.
Step 3: Use the logging feature
Select Disable to stop logging requests.
Select Download to download a zip file containing log text for all logged requests.
Select Clear # of 50 Logs to clear any logged requests and continue logging.
Select Save to save any changes you have made.
Read more about API request logging at the Docusign Support Center.
REQUEST LOGGING
eSignature Dashboard
Docusign also offers an API Dashboard. This tool enables developers to monitor the health of their Docusign integrations, including eSignature REST API requests to the Docusign platform, with the following data:
Detailed reports of failed API requests so you can troubleshoot issues.
Graphical timeline of your successful and failed API requests for a given integration, up to the last 90 days.
Log of the specific API calls made for an integration, which can be filtered by time intervals and response codes.
Details about failed requests that help you to investigate and troubleshoot.
Note: The API Dashboard is available only for users who have access to your API integrations. Other users should use the API Request Logging feature for debugging.
Viewing API Request Data
In the Docusign eSignature app, select Admin, then click Apps and Keys. The API Dashboard section below the Apps and Integrations Keys list displays a summary of requests from your apps.
You can view request data for all apps or for a specific one.
To view a log of recent API requests for the selected app, scroll down below the graph of API activity.
Read more about the API Dashboard at the Docusign Developer Center.
DASHBOARD BASICS
eSignature Usage Center
After your app is live, improving its efficiency can create a better experience for your users and help you avoid bottlenecks that may impact the performance of your app. The Docusign API Usage Center tool helps you understand your application's efficiency, along with recommendations for improving your efficiency score.
To view efficiency scores for all of your apps, select Settings > API Usage Center.
To view issues and recommendations for a specific application from your application list, select Actions > View Efficiency Score.
Viewing Efficiency Scores for All Applications
In the Docusign eSignature app, select Admin, then click API Usage Center. Below the graphs, the API Activity by App section displays an efficiency score for each of your apps.
Viewing Issues and Recommendations for a Specific Application
To view issues and recommendations for a specific application from your application list, select Actions > View Efficiency Score. The API Efficiency page shows the score for your app and details any negative efficiency factors, with links to recommendations for mitigating each factor.
Read more about the API Usage Center at the Docusign Developer Center.
EFFICIENCY BASICS
Go-live with a Custom Integration
Objective: After reviewing this topic, you will be able to submit a Docusign integration to go-live.
When submitting a go-live request, your integration will go through a validation and approval process, which is required for all Docusign developers (customers and partners). You also must set up a production account that has the proper features enabled for your Docusign integration.
There is no cost associated with submitting an application to go-live, but there might be a charge for Docusign production accounts.
The go-live process involves three main steps:
Create your integration.
Request a production account.
Submit your integration to Go Live
Create Your Integration
To create and configure an integration key in your Docusign developer account, complete the following steps:
1
In your browser, navigate to https://developers.docusign.com
2
Click Developer Account in the top right corner.
•
If you have a developer account, click Log in and follow the prompts to log into your account.
•
If you do not have a developer account, click Create account, then follow the prompts to create an account.
3
Navigate to https://apps-d.docusign.com/admin/apps-and-keys
to open the Apps and Keys page for your developer account.
4
Click Add App and Integration Key.
5
Enter a name for your integration, then click Create App.
6
After the heading How will you use this integration?, select the option that applies to your integration.
Note: You must select an option in the How will you use this integration? section before you can complete the go-live process for your integration.
7
Specify any other settings required for your integration, including authentication, redirect URIs, and CORS configuration, then click Save.
Request a Production Account
A Docusign production account is required in order for any integration to go-live. eSignature transactions captured using a developer account are not legally binding. Once your integration moves from the developer environment to the production environment, the integration's eSignature transactions become legally binding.
Verify API Plans and Feature Availability
Ensure Administrator Privileges
Submit Your Integration to Go Live
When you are ready to go live with your integration, follow these steps:
1
Navigate to https://apps-d.docusign.com/admin/apps-and-keys
to open the Apps and Keys page for your developer account.
2
In the Apps and Integration Keys list, click the Actions menu for your integration, then click Start Go live.
3
In the window that opens, enter the login information for the production account that you want to host the integration after it goes live.
4
Select the production account from the list of accounts displayed, then click Select.
Note: If an error message is displayed instead of a list of accounts, this means the integration type you specified while setting up your integration key does not match the account type you logged into. Follow the troubleshooting steps shown in the error message to resolve this issue, then repeat the previous steps.
5
In the Apps and Integration Keys list, your integration now displays the status of your go-live request:
•
App is live: Your integration key is now available in your production account.
•
Pending approval: Your integration requires a manual approval process, which may take up to 48 hours.
Note: The validation and approval process ensures developers use the proper account type and classify their integration keys accurately. In some cases, this process requires manual review by Docusign teams to verify that security, compliance, and quality standards are met.
The Apps and Integration Keys list displays real-time go-live status for all integrations. When your integration passes review and goes live, you can view it in production. If issues are found, you will be asked to make corrections before proceeding.
Note: The go-live process no longer requires making 20 eSign API calls. This means you can start the submission process immediately after setting up an integration.
Lesson 4 - Knowledge Check

Go-live with API Integrations
Go-live Process Overview
Go-live with a Custom Integration
Troubleshooting Your Integration
Knowledge Check
Lesson 2 - Go-live with a Custom Integration
Troubleshooting Your Integration
Objective: After reviewing this topic, you will be able to check API logs and monitor application efficiency.
After your integration goes live, Docusign provides several tools to help you troubleshoot issues you may experience:
eSignature Request Logging
eSignature Dashboard
eSignature Usage Center
eSignature Request Logging
The API request logging feature is not enabled by default. You must enable the logs first to get the updates. You can check the API logs via a web application or API logging tool. Docusign recommends checking API logs periodically to ensure the accuracy of your requests and responses. Review the following steps for enabling, viewing or clearing API logs within the Docusign eSignature app.
Note:
Request logging is available to all users, not just developers. Wide availability allows your support staff to debug problems with your user account.
Step 1: Navigate to the account settings
Select the account icon showing your initials at the top right, then select My Preferences.
Step 2: Enable the logging feature
Select Enable Logging to begin logging API requests for your account.
Step 3: Use the logging feature
Select Disable to stop logging requests.
Select Download to download a zip file containing log text for all logged requests.
Select Clear # of 50 Logs to clear any logged requests and continue logging.
Select Save to save any changes you have made.
Read more about API request logging at the Docusign Support Center.
REQUEST LOGGING
eSignature Dashboard
Docusign also offers an API Dashboard. This tool enables developers to monitor the health of their Docusign integrations, including eSignature REST API requests to the Docusign platform, with the following data:
Detailed reports of failed API requests so you can troubleshoot issues.
Graphical timeline of your successful and failed API requests for a given integration, up to the last 90 days.
Log of the specific API calls made for an integration, which can be filtered by time intervals and response codes.
Details about failed requests that help you to investigate and troubleshoot.
Note: The API Dashboard is available only for users who have access to your API integrations. Other users should use the API Request Logging feature for debugging.
Viewing API Request Data
In the Docusign eSignature app, select Admin, then click Apps and Keys. The API Dashboard section below the Apps and Integrations Keys list displays a summary of requests from your apps.
You can view request data for all apps or for a specific one.
To view a log of recent API requests for the selected app, scroll down below the graph of API activity.
Read more about the API Dashboard at the Docusign Developer Center.
DASHBOARD BASICS
eSignature Usage Center
After your app is live, improving its efficiency can create a better experience for your users and help you avoid bottlenecks that may impact the performance of your app. The Docusign API Usage Center tool helps you understand your application's efficiency, along with recommendations for improving your efficiency score.
To view efficiency scores for all of your apps, select Settings > API Usage Center.
To view issues and recommendations for a specific application from your application list, select Actions > View Efficiency Score.
Viewing Efficiency Scores for All Applications
In the Docusign eSignature app, select Admin, then click API Usage Center. Below the graphs, the API Activity by App section displays an efficiency score for each of your apps.
Viewing Issues and Recommendations for a Specific Application
To view issues and recommendations for a specific application from your application list, select Actions > View Efficiency Score. The API Efficiency page shows the score for your app and details any negative efficiency factors, with links to recommendations for mitigating each factor.
Read more about the API Usage Center at the Docusign Developer Center.
EFFICIENCY BASICS
Lesson 4 - Knowledge Check

Go-live with API Integrations
Go-live Process Overview
Go-live with a Custom Integration
Troubleshooting Your Integration
Knowledge Check
Go-live with a Custom Integration
Objective: After reviewing this topic, you will be able to submit a Docusign integration to go-live.
When submitting a go-live request, your integration will go through a validation and approval process, which is required for all Docusign developers (customers and partners). You also must set up a production account that has the proper features enabled for your Docusign integration.
There is no cost associated with submitting an application to go-live, but there might be a charge for Docusign production accounts.
The go-live process involves three main steps:
Create your integration.
Request a production account.
Submit your integration to Go Live
Create Your Integration
To create and configure an integration key in your Docusign developer account, complete the following steps:
1
In your browser, navigate to https://developers.docusign.com
2
Click Developer Account in the top right corner.
•
If you have a developer account, click Log in and follow the prompts to log into your account.
•
If you do not have a developer account, click Create account, then follow the prompts to create an account.
3
Navigate to https://apps-d.docusign.com/admin/apps-and-keys
to open the Apps and Keys page for your developer account.
4
Click Add App and Integration Key.
5
Enter a name for your integration, then click Create App.
6
After the heading How will you use this integration?, select the option that applies to your integration.
Note: You must select an option in the How will you use this integration? section before you can complete the go-live process for your integration.
7
Specify any other settings required for your integration, including authentication, redirect URIs, and CORS configuration, then click Save.
Request a Production Account
A Docusign production account is required in order for any integration to go-live. eSignature transactions captured using a developer account are not legally binding. Once your integration moves from the developer environment to the production environment, the integration's eSignature transactions become legally binding.
Verify API Plans and Feature Availability
Ensure Administrator Privileges
Submit Your Integration to Go Live
When you are ready to go live with your integration, follow these steps:
1
Navigate to https://apps-d.docusign.com/admin/apps-and-keys
to open the Apps and Keys page for your developer account.
2
In the Apps and Integration Keys list, click the Actions menu for your integration, then click Start Go live.
3
In the window that opens, enter the login information for the production account that you want to host the integration after it goes live.
4
Select the production account from the list of accounts displayed, then click Select.
Note: If an error message is displayed instead of a list of accounts, this means the integration type you specified while setting up your integration key does not match the account type you logged into. Follow the troubleshooting steps shown in the error message to resolve this issue, then repeat the previous steps.
5
In the Apps and Integration Keys list, your integration now displays the status of your go-live request:
•
App is live: Your integration key is now available in your production account.
•
Pending approval: Your integration requires a manual approval process, which may take up to 48 hours.
Note: The validation and approval process ensures developers use the proper account type and classify their integration keys accurately. In some cases, this process requires manual review by Docusign teams to verify that security, compliance, and quality standards are met.
The Apps and Integration Keys list displays real-time go-live status for all integrations. When your integration passes review and goes live, you can view it in production. If issues are found, you will be asked to make corrections before proceeding.
Note: The go-live process no longer requires making 20 eSign API calls. This means you can start the submission process immediately after setting up an integration.
Troubleshooting Your Integration
Objective: After reviewing this topic, you will be able to check API logs and monitor application efficiency.
After your integration goes live, Docusign provides several tools to help you troubleshoot issues you may experience:
eSignature Request Logging
eSignature Dashboard
eSignature Usage Center
eSignature Request Logging
The API request logging feature is not enabled by default. You must enable the logs first to get the updates. You can check the API logs via a web application or API logging tool. Docusign recommends checking API logs periodically to ensure the accuracy of your requests and responses. Review the following steps for enabling, viewing or clearing API logs within the Docusign eSignature app.
Note:
Request logging is available to all users, not just developers. Wide availability allows your support staff to debug problems with your user account.
Step 1: Navigate to the account settings
Select the account icon showing your initials at the top right, then select My Preferences.
Step 2: Enable the logging feature
Select Enable Logging to begin logging API requests for your account.
Step 3: Use the logging feature
Select Disable to stop logging requests.
Select Download to download a zip file containing log text for all logged requests.
Select Clear # of 50 Logs to clear any logged requests and continue logging.
Select Save to save any changes you have made.
Read more about API request logging at the Docusign Support Center.
REQUEST LOGGING
eSignature Dashboard
Docusign also offers an API Dashboard. This tool enables developers to monitor the health of their Docusign integrations, including eSignature REST API requests to the Docusign platform, with the following data:
Detailed reports of failed API requests so you can troubleshoot issues.
Graphical timeline of your successful and failed API requests for a given integration, up to the last 90 days.
Log of the specific API calls made for an integration, which can be filtered by time intervals and response codes.
Details about failed requests that help you to investigate and troubleshoot.
Note: The API Dashboard is available only for users who have access to your API integrations. Other users should use the API Request Logging feature for debugging.
Viewing API Request Data
In the Docusign eSignature app, select Admin, then click Apps and Keys. The API Dashboard section below the Apps and Integrations Keys list displays a summary of requests from your apps.
You can view request data for all apps or for a specific one.
To view a log of recent API requests for the selected app, scroll down below the graph of API activity.
Read more about the API Dashboard at the Docusign Developer Center.
DASHBOARD BASICS
eSignature Usage Center
After your app is live, improving its efficiency can create a better experience for your users and help you avoid bottlenecks that may impact the performance of your app. The Docusign API Usage Center tool helps you understand your application's efficiency, along with recommendations for improving your efficiency score.
To view efficiency scores for all of your apps, select Settings > API Usage Center.
To view issues and recommendations for a specific application from your application list, select Actions > View Efficiency Score.
Viewing Efficiency Scores for All Applications
In the Docusign eSignature app, select Admin, then click API Usage Center. Below the graphs, the API Activity by App section displays an efficiency score for each of your apps.
Viewing Issues and Recommendations for a Specific Application
To view issues and recommendations for a specific application from your application list, select Actions > View Efficiency Score. The API Efficiency page shows the score for your app and details any negative efficiency factors, with links to recommendations for mitigating each factor.
Read more about the API Usage Center at the Docusign Developer Center.
EFFICIENCY BASICS
Lesson 3 - Troubleshooting Your Integration

Go-live with API Integrations
Go-live Process Overview
Go-live with a Custom Integration
Troubleshooting Your Integration
Knowledge Check
Lesson 1 - Go-live Process Overview
Go-live with a Custom Integration
Objective: After reviewing this topic, you will be able to submit a Docusign integration to go-live.
When submitting a go-live request, your integration will go through a validation and approval process, which is required for all Docusign developers (customers and partners). You also must set up a production account that has the proper features enabled for your Docusign integration.
There is no cost associated with submitting an application to go-live, but there might be a charge for Docusign production accounts.
The go-live process involves three main steps:
Create your integration.
Request a production account.
Submit your integration to Go Live
Create Your Integration
To create and configure an integration key in your Docusign developer account, complete the following steps:
1
In your browser, navigate to https://developers.docusign.com
2
Click Developer Account in the top right corner.
•
If you have a developer account, click Log in and follow the prompts to log into your account.
•
If you do not have a developer account, click Create account, then follow the prompts to create an account.
3
Navigate to https://apps-d.docusign.com/admin/apps-and-keys
to open the Apps and Keys page for your developer account.
4
Click Add App and Integration Key.
5
Enter a name for your integration, then click Create App.
6
After the heading How will you use this integration?, select the option that applies to your integration.
Note: You must select an option in the How will you use this integration? section before you can complete the go-live process for your integration.
7
Specify any other settings required for your integration, including authentication, redirect URIs, and CORS configuration, then click Save.
Request a Production Account
A Docusign production account is required in order for any integration to go-live. eSignature transactions captured using a developer account are not legally binding. Once your integration moves from the developer environment to the production environment, the integration's eSignature transactions become legally binding.
Verify API Plans and Feature Availability
Developer accounts may have features that are not available in your production environment without purchasing a higher-tier product. Make sure that you've selected the right API Plan for the features you need. If you're using a different Docusign plan for your application, check with your Docusign business or technical contact.
When purchasing a plan, make sure the plan you have selected includes all of the features necessary for your integration; for example, Basic Data Verification is included only with certain plans. It is likely that your integration will not work as expected if your production account does not include all of the features that your app relied on in the developer environment.
Ensure Administrator Privileges
Submit Your Integration to Go Live
When you are ready to go live with your integration, follow these steps:
1
Navigate to https://apps-d.docusign.com/admin/apps-and-keys
to open the Apps and Keys page for your developer account.
2
In the Apps and Integration Keys list, click the Actions menu for your integration, then click Start Go live.
3
In the window that opens, enter the login information for the production account that you want to host the integration after it goes live.
4
Select the production account from the list of accounts displayed, then click Select.
Note: If an error message is displayed instead of a list of accounts, this means the integration type you specified while setting up your integration key does not match the account type you logged into. Follow the troubleshooting steps shown in the error message to resolve this issue, then repeat the previous steps.
5
In the Apps and Integration Keys list, your integration now displays the status of your go-live request:
•
App is live: Your integration key is now available in your production account.
•
Pending approval: Your integration requires a manual approval process, which may take up to 48 hours.
Note: The validation and approval process ensures developers use the proper account type and classify their integration keys accurately. In some cases, this process requires manual review by Docusign teams to verify that security, compliance, and quality standards are met.
The Apps and Integration Keys list displays real-time go-live status for all integrations. When your integration passes review and goes live, you can view it in production. If issues are found, you will be asked to make corrections before proceeding.
Note: The go-live process no longer requires making 20 eSign API calls. This means you can start the submission process immediately after setting up an integration.
Lesson 3 - Troubleshooting Your Integration

Go-live with API Integrations
Go-live Process Overview
Go-live with a Custom Integration
Troubleshooting Your Integration
Knowledge Check
Lesson 1 - Go-live Process Overview
Go-live with a Custom Integration
Objective: After reviewing this topic, you will be able to submit a Docusign integration to go-live.
When submitting a go-live request, your integration will go through a validation and approval process, which is required for all Docusign developers (customers and partners). You also must set up a production account that has the proper features enabled for your Docusign integration.
There is no cost associated with submitting an application to go-live, but there might be a charge for Docusign production accounts.
The go-live process involves three main steps:
Create your integration.
Request a production account.
Submit your integration to Go Live
Create Your Integration
To create and configure an integration key in your Docusign developer account, complete the following steps:
1
In your browser, navigate to https://developers.docusign.com
2
Click Developer Account in the top right corner.
•
If you have a developer account, click Log in and follow the prompts to log into your account.
•
If you do not have a developer account, click Create account, then follow the prompts to create an account.
3
Navigate to https://apps-d.docusign.com/admin/apps-and-keys
to open the Apps and Keys page for your developer account.
4
Click Add App and Integration Key.
5
Enter a name for your integration, then click Create App.
6
After the heading How will you use this integration?, select the option that applies to your integration.
Note: You must select an option in the How will you use this integration? section before you can complete the go-live process for your integration.
7
Specify any other settings required for your integration, including authentication, redirect URIs, and CORS configuration, then click Save.
Request a Production Account
A Docusign production account is required in order for any integration to go-live. eSignature transactions captured using a developer account are not legally binding. Once your integration moves from the developer environment to the production environment, the integration's eSignature transactions become legally binding.
Verify API Plans and Feature Availability
Developer accounts may have features that are not available in your production environment without purchasing a higher-tier product. Make sure that you've selected the right API Plan for the features you need. If you're using a different Docusign plan for your application, check with your Docusign business or technical contact.
When purchasing a plan, make sure the plan you have selected includes all of the features necessary for your integration; for example, Basic Data Verification is included only with certain plans. It is likely that your integration will not work as expected if your production account does not include all of the features that your app relied on in the developer environment.
Ensure Administrator Privileges
When setting up a Docusign production account, the developer submitting the go-live request must have administrator privileges on the production account. Make sure the submitting developer's privileges are conﬁgured before submitting an integration for review.
Submit Your Integration to Go Live
When you are ready to go live with your integration, follow these steps:
1
Navigate to https://apps-d.docusign.com/admin/apps-and-keys
to open the Apps and Keys page for your developer account.
2
In the Apps and Integration Keys list, click the Actions menu for your integration, then click Start Go live.
3
In the window that opens, enter the login information for the production account that you want to host the integration after it goes live.
4
Select the production account from the list of accounts displayed, then click Select.
Note: If an error message is displayed instead of a list of accounts, this means the integration type you specified while setting up your integration key does not match the account type you logged into. Follow the troubleshooting steps shown in the error message to resolve this issue, then repeat the previous steps.
5
In the Apps and Integration Keys list, your integration now displays the status of your go-live request:
•
App is live: Your integration key is now available in your production account.
•
Pending approval: Your integration requires a manual approval process, which may take up to 48 hours.
Note: The validation and approval process ensures developers use the proper account type and classify their integration keys accurately. In some cases, this process requires manual review by Docusign teams to verify that security, compliance, and quality standards are met.
The Apps and Integration Keys list displays real-time go-live status for all integrations. When your integration passes review and goes live, you can view it in production. If issues are found, you will be asked to make corrections before proceeding.
Note: The go-live process no longer requires making 20 eSign API calls. This means you can start the submission process immediately after setting up an integration.
Lesson 3 - Troubleshooting Your Integration

## Create and Configure Envelopes with the eSignature API

### Build Envelopes and Use Templates with the eSignature API 30 min

Build Envelopes and Use Templates with the eSignature API
Envelope Concepts and Models
Construct an eSignature REST API Call to Create an Envelope
DIRECT DOCUMENTS MODEL
Create Requests for the Direct Documents Model
TEMPLATE REFERENCE MODEL
Create Requests for the Template Reference Model
COMPOSITE TEMPLATES MODEL
Create Requests for the Composite Templates Model
ACTIVITY
Activity: Create Envelopes with API Calls
Lesson 3 - Create Requests for the Direct Documents Model
Create Requests for the Template Reference Model
Objective: After reviewing this topic, you will be able to build the JSON body for a call to the eSignature REST API using the template reference model.
When you create an API request using the template reference model, you can include a single template. Docusign offers two main types of eSignature templates: standard envelope templates and document generation templates.
Standard envelope templates
Document generation templates
The process for creating and sending an envelope with the API is different depending on which template type you use.
Note: To learn about the advantages of each template type and how to create them, enroll in the Create Docusign Templates to Simplify Sending course at Docusign University.
Best Practice
Templates are typically set up once and then referenced, and Docusign recommends doing this initial setup in the Docusign eSignature app for each template, then referencing templates by ID in your API calls as needed. Although it is possible to create a template using an API call, it can be cumbersome to place Docusign tags within a document programmatically.
To send an envelope using a standard envelope template or a document generation template, you make a POST request to the Envelopes: create endpoint
, passing the template ID and other required properties.
Required JSON body properties
A request to create an envelope using a template includes values for three required JSON body properties:
STATUS
TEMPLATEID
TEMPLATEROLES
The status property specifies the initial envelope status, which is either "created" or "sent".
When using the "created" status, the envelope is not sent to recipients, and remains in a draft stage until the status is set to "sent".
When using the "sent" status, the envelope is created and immediately sent to all attached recipients in their defined routing order.
Note: To send with a document generation template, the first step is to create a draft envelope using a status of "created." You then use additional requests to add document generation field values to the envelope before changing the status to "sent."
You can retrieve the value for templateId by opening the template in the Docusign app and clicking the copy icon next to the template ID value.
You can also get this value by making an API request to the Templates: list endpoint
Note: Template ID values are different between developer and production accounts, so be sure to update these values as part of the go-live process for your integration.
Send with a Standard Envelope Template
To send an envelope with a standard envelope template, you simply make a POST request to the Envelopes: create
endpoint with the JSON body and the headers.
After your request is received, the envelope is authenticated against the associated Docusign accountId, then the envelope is created, the template is applied, and the envelope is sent to all recipients in the routing order defined by the template.
Send with a Document Generation Template
The process to send an envelope with a document generation template includes four main steps:
1
Create a draft envelope
2
Retrieve placeholder fields
3
Populate field values
4
Send the envelope
Create a draft envelope
To create an envelope definition from a document generation template, you make a POST request to the Envelopes: create
endpoint. You must specify values for templateId, templateRoles, and status, and the status value must be created.
Retrieve placeholder fields
To retrieve a list of the placeholder fields available on the template, you make a GET request to the DocumentGeneration: getEnvelopeDocGenFormFields
endpoint:
/restapi/v2.1/accounts/{accountId}/envelopes/{envelopeId}/docGenFormFields
The response includes all the fields available on your document including their label, type, required vs optional property, and name, as well as the document id.
The following JSON code shows example response data:
{
"docGenFormFields": [
{
"documentId": "b83617f9-xxxx-xxxx-xxxx-d5dda0ba77e6",
"docGenFormFieldList": [
{
"label": "Candidate_Name",
"type": "TextBox",
"required": "True",
"name": "Candidate_Name"
},
{
"label": "Job_Title",
"type": "TextBox",
"required": "True",
"name": "Job_Title"
},
{
"label": "Start_Date",
"type": "TextBox",
"required": "True",
"name": "Start_Date"
},
{
"label": "Annual_Salary",
"type": "TextBox",
"required": "True",
"name": "Annual_Salary"
}
],
"docGenDocumentStatus": "created"
}
]
}
Note: If your template contains a dynamic table, the response will include a rowValues.docGenFormFieldList array. This array defines the sender fields that make up the table row definition. For more information review the Developer Center guide
Populate field values
To populate the template fields with values, you make a PUT request to the DocumentGeneration: updateEnvelopeDocGenFormFields
endpoint:
/restapi/v2.1/accounts/{accountId}/envelopes/{envelopeId}/docGenFormFields
Your request body must reference the field names returned in the response to the previous request, and must provide a value for each required field.
The following JSON code shows an example request body:
{
"docGenFormFields": [
{
"documentId": "667017ec-xxxx-xxxx-xxxx-f1cc1a8fc11d",
"docGenFormFieldList": [
{
"name": "Candidate_Name",
"value": "Caroline Miller"
},
{
"name": "Job_Title",
"value": "Software Engineer"
},
{
"name": "Start_Date",
"value": "07/10/2023"
},
{
"name": "Annual_Salary",
"value": "$120,000"
}
],
"docGenDocumentStatus": "created"
}
]
}
If your document generation file includes conditional content, it will be applied during this step.
Send the envelope
To send the draft envelope for signature, you make a PUT request to the Envelopes: update
endpoint and set the "status" to "sent":
/restapi/v2.1/accounts/{accountId}/envelopes/{envelopeId}
{
"status": "sent"
}
After your request is received, the envelope is sent to all recipients in the routing order defined by the template.
Lesson 5 - Create Requests for the Composite Templates Model

Build Envelopes and Use Templates with the eSignature API
RESUME COURSE
Welcome to the Build Envelopes and Use Templates with the eSignature API course. After reviewing this course, you will be able to:
Explain the tradeoffs between different forms of envelope structure.
Build API requests for envelopes using direct documents, template references, and composite templates.
Envelope Concepts and Models
Construct an eSignature REST API Call to Create an Envelope
DIRECT DOCUMENTS MODEL
Create Requests for the Direct Documents Model
TEMPLATE REFERENCE MODEL
Create Requests for the Template Reference Model
COMPOSITE TEMPLATES MODEL
Create Requests for the Composite Templates Model
ACTIVITY
Activity: Create Envelopes with API Calls

Build Envelopes and Use Templates with the eSignature API
Envelope Concepts and Models
Construct an eSignature REST API Call to Create an Envelope
DIRECT DOCUMENTS MODEL
Create Requests for the Direct Documents Model
TEMPLATE REFERENCE MODEL
Create Requests for the Template Reference Model
COMPOSITE TEMPLATES MODEL
Create Requests for the Composite Templates Model
ACTIVITY
Activity: Create Envelopes with API Calls
Lesson 5 - Create Requests for the Composite Templates Model
Activity: Create Envelopes with API Calls
In this activity, you will upload envelope templates and perform a sequence of API requests to send envelopes using the eSignature API with direct documents, server templates, document generation server template, and composite templates.
Follow the steps below to complete the activity. The steps are sequenced and must be completed in order. This activity can be completed in 15 minutes.
Setup
To complete this activity, you need two resources:
Docusign developer account: If you don't already have one, create a developer account
on the Docusign Developer Center.
Postman: Download Postman
for free and install it on your computer, or use the online version
Upload Templates
Download the following JSON files, which contain Docusign envelope templates:
InspectionAddendum.json
205.9 KB
NDA.json
300 KB
OfferLetter.json
3.2 MB
SellerDisclosure.json
226.3 KB
Navigate to your Docusign developer account, click the Templates tab, click Start > Envelope Templates > Upload Template, and then upload the InspectionAddendum.json file.
Repeat the previous step to upload NDA.json, OfferLetter.json, and SellerDisclosure.json.
Configure Postman and Your Docusign Integration
Download the following Postman collection and environment, then import them into a new workspace in Postman:
Build Envelopes and Use Templates with the eSignature API.postman_collection.json
18 KB
Build Envelopes and Use Templates with the eSignature API.postman_environment.json
122.9 KB
Specify the Build Envelopes and Use Templates with the eSignature API environment as the active environment.
In your browser, log in to your Docusign developer account, then under Settings, in the Apps & Keys section, create a new app.
On the app settings page, in the Integration Type section, choose a classification for your app.
Note: To learn more about the different classifications, explore the Docusign Go-live
process on the Docusign Developer Center.
Click Add Secret Key to create a secret key, then copy the value.
In Postman, open the Build Envelopes and Use Templates with the eSignature API environment, then paste your secret key as the value of the iSec variable.
In the Docusign settings for your new app, copy the value of your Integration Key, then paste it as the value of the iKey variable in Postman.
In the Docusign settings for your new app, click Add Uri, enter https://oauth.pstmn.io/v1/browser-callback, then click Save to save your changes to the app configuration.
Click the Templates tab, open the NDA template that you uploaded, click the Copy icon next to the template ID, then in Postman paste the value you copied as the value of the NDATemplateId variable.
Repeat the previous step for the Inspection Addendum, Offer Letter, and Seller Disclosure templates.
In the Postman environment, enter your email address for the value of the PaulMartinEmail and MariaGarciaEmail variables.
Select the Build Envelopes and Use Templates with the eSignature API collection folder, then on the Auth or Authorization tab, click Get New Access Token. Follow the prompts to log into your Docusign developer account and grant permission to Postman to make requests on your behalf, then click Use Token to use the access token.
Within the Build Envelopes and Use Templates with the eSignature API collection folder, open the Setup folder, then click the Get User Info request to verify that you have a valid access token and to retrieve basic information about your Docusign account.
Send the request, open the Build Envelopes and Use Templates with the eSignature API environment, then verify that the environment now includes values for the userId, baseUrl, and accountId variables.
Note: If the variable values are empty, send the Get User Info request again and recheck the variables..
Send an Envelope using the Direct Documents Model
In Postman, open the Build Envelopes and Use Templates with the eSignature API collection, open the Direct Documents folder, then click the 01 - Send an envelope using a direct document request.
Click the Body tab, then examine the request body.
Note: The document has been base-64 encoded and stored in the NDAPDFBytes environment variable.
Click Send, then verify that you receive a response value of 201 Created.
In your email, open the notification message, click the link to start the signing process, examine the document and signer tabs, then complete the signing process.
Send an Envelope using the Template Reference Model
In Postman, open the Template Reference folder, then click the 02 - Send an envelope using a template reference request.
Click the Body tab, then examine the request body.
Note: The envelope uses the NDA template you uploaded to your account. You copied the template ID value to the NDATemplateId environment variable in an earlier step. The signer tabs are already specified in the template itself, so they're not included in the request body.
Click Send, then verify that you receive a response value of 201 Created.
In your email, open the notification message, click the link to start the signing process, examine the document and signer tabs, then complete the signing process.
Send an Envelope using the Document Generation Template Reference Model
In Postman, open the Document Generation Template Reference folder, then click the 03 - Send a draft document generation envelope request.
Click the Body tab, then examine the request body.
Note: The envelope uses the Offer Letter template you uploaded to your account. You copied the template ID value to the OfferLetterTemplateId environment variable in an earlier step.
Click Send, then verify that you receive a response value of 201 Created.
Note: The Postman request includes a post-request script that saves the returned documentId to an environment variable for use in later requests.
Click the 04 - Get document generation fields request, click Send, verify that you receive a response value of 200 OK, then review the document generation field data in the response.
Review the field data in the response.
Click the 05 - Update document generation field values request, click the Body tab, then examine the structure and content of the request body.
Click Send, verify that you receive a response value of 200 OK, then review the response data.
Click the 06 - Send document generation envelope request, click the Body tab, then review the request body, which changes the envelope status from created to sent.
Click Send, verify that you receive a response value of 200 OK.
In your email, open the notification message, click the link to start the signing process, examine the generated document, then complete the signing process.
Send an Envelope using the Composite Templates Model
In Postman, open the Composite Templates folder, then click the 07 - Send an envelope using composite templates request.
Click the Body tab, then examine the request body.
Note: The envelope uses the base64-encoded Cover Letter document stored in the CoverLetterBytes environment variable, as well as the Inspection Addendum and Seller Disclosure templates you uploaded to your account.
Click Send, then verify that you receive a response value of 201 Created.
In your email, open the notification message, click the link to start the signing process, examine the documents, document order, and signer tabs, then complete the signing process.

Build Envelopes and Use Templates with the eSignature API
Envelope Concepts and Models
Construct an eSignature REST API Call to Create an Envelope
DIRECT DOCUMENTS MODEL
Create Requests for the Direct Documents Model
TEMPLATE REFERENCE MODEL
Create Requests for the Template Reference Model
COMPOSITE TEMPLATES MODEL
Create Requests for the Composite Templates Model
ACTIVITY
Activity: Create Envelopes with API Calls
Lesson 1 - Envelope Concepts and Models
Construct an eSignature REST API Call to Create an Envelope
Objective: After reviewing this topic, you will be able to build a call to the eSignature REST API to create an envelope.
Base URI
You request user information from the Envelopes: create endpoint
at the following path:
{baseUri}/{apiVersion}/accounts/{accountId}/envelopes
Like other URIs for other Docusign endpoints, the base URI for creating an envelope varies depending on whether your app is in development or is deployed to production:
Development
https://demo.docusign.net/restapi
Production
https://{site}.docusign.net/restapi
where {site} is the Docusign site that hosts your account, such as na3, eu, or au
Note:
All examples in this course use development endpoints. When deploying your app to production, ensure that you update all instances of the URI to use production endpoints.
The accountId parameter is the Docusign account ID for the account making the API call, which varies between development and production accounts. To programmatically retrieve this value, you call the oauth/userinfo endpoint after completing a supported OAuth flow.
Note: To learn about the OAuth flows supported by Docusign and how to integrate them into your app, enroll in the "Implement Authentication with Docusign APIs" self-paced learning plan in Docusign University.
JSON Body
The required JSON body properties to create an envelope vary depending on whether you are using the direct documents, template reference, or composite template model. You will review each of these JSON structures and their properties later in this course.
Required Headers
A request to create an envelope must include two required headers:
AUTHORIZATION
CONTENT-TYPE
The Authorization header value must include the word Bearer followed by a valid access token obtained using an OAuth2 flow.
Request
To create an envelope, you make a POST request to the Envelopes: create endpoint
with the JSON body and the headers.
Response
The returned response supplies you with an envelopeId value for the newly created envelope, along with a URI snippet for the envelope, the envelope status, and a time stamp.
Lesson 3 - Create Requests for the Direct Documents Model

Build Envelopes and Use Templates with the eSignature API
Envelope Concepts and Models
Construct an eSignature REST API Call to Create an Envelope
DIRECT DOCUMENTS MODEL
Create Requests for the Direct Documents Model
TEMPLATE REFERENCE MODEL
Create Requests for the Template Reference Model
COMPOSITE TEMPLATES MODEL
Create Requests for the Composite Templates Model
ACTIVITY
Activity: Create Envelopes with API Calls
Envelope Concepts and Models
Objective: After reviewing this topic, you’ll be able to describe the components of an eSignature envelope and the envelope types that the eSignature API supports.
Docusign eSignature envelopes are built using a set of basic objects. You can combine these objects to build envelopes using the Docusign eSignature API based on a few different envelope models.
Envelope Concepts
Envelope Objects
Every agreement you send with Docusign eSignature is made up of four objects: envelope, document, recipient, and tab.
Envelope
Document
Recipient
Tab
Envelope Templates
An envelope template is a preconfigured envelope structure you configure with documents, recipient roles, and tabs, and then reuse when you need to complete the same agreement process with different recipients.
The Docusign app is the easiest way to create and configure an envelope template. However, after you have created and saved a template to your account, you can reference it in API calls to build and send envelopes.
Document Generation Templates
A document generation template is a specialized envelope template where traditional field data is embedded seamlessly into the agreement. Document information is dynamically populated, generating final documents that are professional-looking and well formatted. A document generation template can also include conditional logic to show or hide sections based on the data supplied for a specific transaction.
Document generation templates are created and managed separately from standard envelope templates in the Docusign app. However, you can incorporate both of these types of envelope templates in eSignature API requests to build and send envelopes.
Envelope Models
When you build an envelope using the Docusign eSignature REST API, you have a few models to choose from for your envelope structure:
Direct documents model
Template reference model
Composite templates model
Direct Documents Model
Using the direct documents model, you build an envelope entirely from scratch in an API call, providing documents, recipients, and tabs within your request.
Advantage: When your integration has only basic needs, this type of solution can be quick to build.
Drawback: Because this approach uses no templates, the resulting envelope is not very flexible, and can require significant work to expand or replace as the needs of your integration change and grow.
The following code shows the JSON body for a create envelope request using the direct documents model:
Template Reference Model
When your API call uses the template reference model, you reference a single envelope template built in the Docusign app.
Advantage: This approach enables you to create an envelope using a single envelope template, which can be useful for a basic use case.
Drawback: An envelope using this model cannot be expanded to use multiple envelope templates, so it does not provide flexibility as the needs of your users grow.
The following code shows the JSON body for a create envelope request using the template reference model:
Composite Templates Model
An envelope built using the composite templates model supports the features of both the direct documents and template reference model, along with additional options. This model provides the option to directly specify a document, to apply one or more server templates, and to provide additional details inline within a single envelope.
Advantage: The composite templates model supports any use case that the simpler models can address, as well as some situations that they can't handle. Even for basic use cases, creating an integration with a composite template builds in the flexibility to easily expand or enhance the solution later on without needing to rewrite it from the ground up.
Drawback: Implementing the composite templates model can require planning and troubleshooting, which can be a challenge to incorporate into a tight schedule.
Note: The composite templates model is built around an array of objects in the API request body. Each object in the array can directly specify a document, apply one or more envelope templates, and provide additional details inline. An object in this array is referred to as a template object. However, this is a separate concept from an envelope template that you create in the Docusign app. The template objects that make up the structure of the composite template model are created only within the body of an API call.
The following code shows the JSON body for a create envelope request using the composite templates model:
Choosing an Envelope Model
Direct documents: For a basic integration that doesn't require a template, using this approach can allow you to code up and deploy a solution quickly.
Template reference: When your requirements call for only a single template, using this model enables you to build a straightforward solution in with minimal coding.
Composite templates: When neither of the more basic approaches can meet the needs of your project, then this model is the obvious choice. In addition, if your organization is planning to grow your use of Docusign eSignature moving forward, then choosing the composite templates approach for more basic needs ensures that you'll have the architecture in place to scale and modify your integration in the future as your requirements change.
Construct an eSignature REST API Call to Create an Envelope
Objective: After reviewing this topic, you will be able to build a call to the eSignature REST API to create an envelope.
Base URI
You request user information from the Envelopes: create endpoint
at the following path:
{baseUri}/{apiVersion}/accounts/{accountId}/envelopes
Like other URIs for other Docusign endpoints, the base URI for creating an envelope varies depending on whether your app is in development or is deployed to production:
Development
https://demo.docusign.net/restapi
Production
https://{site}.docusign.net/restapi
where {site} is the Docusign site that hosts your account, such as na3, eu, or au
Note:
All examples in this course use development endpoints. When deploying your app to production, ensure that you update all instances of the URI to use production endpoints.
The accountId parameter is the Docusign account ID for the account making the API call, which varies between development and production accounts. To programmatically retrieve this value, you call the oauth/userinfo endpoint after completing a supported OAuth flow.
Note: To learn about the OAuth flows supported by Docusign and how to integrate them into your app, enroll in the "Implement Authentication with Docusign APIs" self-paced learning plan in Docusign University.
JSON Body
The required JSON body properties to create an envelope vary depending on whether you are using the direct documents, template reference, or composite template model. You will review each of these JSON structures and their properties later in this course.
Required Headers
A request to create an envelope must include two required headers:
AUTHORIZATION
CONTENT-TYPE
The Authorization header value must include the word Bearer followed by a valid access token obtained using an OAuth2 flow.
Request
To create an envelope, you make a POST request to the Envelopes: create endpoint
with the JSON body and the headers.
Response
The returned response supplies you with an envelopeId value for the newly created envelope, along with a URI snippet for the envelope, the envelope status, and a time stamp.
Lesson 2 - Construct an eSignature REST API Call to Create an Envelope

Build Envelopes and Use Templates with the eSignature API
Envelope Concepts and Models
Construct an eSignature REST API Call to Create an Envelope
DIRECT DOCUMENTS MODEL
Create Requests for the Direct Documents Model
TEMPLATE REFERENCE MODEL
Create Requests for the Template Reference Model
COMPOSITE TEMPLATES MODEL
Create Requests for the Composite Templates Model
ACTIVITY
Activity: Create Envelopes with API Calls
Envelope Concepts and Models
Objective: After reviewing this topic, you’ll be able to describe the components of an eSignature envelope and the envelope types that the eSignature API supports.
Docusign eSignature envelopes are built using a set of basic objects. You can combine these objects to build envelopes using the Docusign eSignature API based on a few different envelope models.
Envelope Concepts
Envelope Objects
Every agreement you send with Docusign eSignature is made up of four objects: envelope, document, recipient, and tab.
Envelope
Document
A document is a digital file whose content must be reviewed, signed, approved, or initialed by one or more recipients.
Documents can be uploaded from a device or added from a cloud storage system.
Docusign accepts a wide variety of document types, including PDF, DOCX, RTF, and PNG.
You can include multiple documents in a single envelope.
Documents are always encrypted while stored in the system.
Recipient
Tab
Envelope Templates
An envelope template is a preconfigured envelope structure you configure with documents, recipient roles, and tabs, and then reuse when you need to complete the same agreement process with different recipients.
The Docusign app is the easiest way to create and configure an envelope template. However, after you have created and saved a template to your account, you can reference it in API calls to build and send envelopes.
Document Generation Templates
A document generation template is a specialized envelope template where traditional field data is embedded seamlessly into the agreement. Document information is dynamically populated, generating final documents that are professional-looking and well formatted. A document generation template can also include conditional logic to show or hide sections based on the data supplied for a specific transaction.
Document generation templates are created and managed separately from standard envelope templates in the Docusign app. However, you can incorporate both of these types of envelope templates in eSignature API requests to build and send envelopes.
Envelope Models
When you build an envelope using the Docusign eSignature REST API, you have a few models to choose from for your envelope structure:
Direct documents model
Template reference model
Composite templates model
Direct Documents Model
Using the direct documents model, you build an envelope entirely from scratch in an API call, providing documents, recipients, and tabs within your request.
Advantage: When your integration has only basic needs, this type of solution can be quick to build.
Drawback: Because this approach uses no templates, the resulting envelope is not very flexible, and can require significant work to expand or replace as the needs of your integration change and grow.
The following code shows the JSON body for a create envelope request using the direct documents model:
Template Reference Model
When your API call uses the template reference model, you reference a single envelope template built in the Docusign app.
Advantage: This approach enables you to create an envelope using a single envelope template, which can be useful for a basic use case.
Drawback: An envelope using this model cannot be expanded to use multiple envelope templates, so it does not provide flexibility as the needs of your users grow.
The following code shows the JSON body for a create envelope request using the template reference model:
Composite Templates Model
An envelope built using the composite templates model supports the features of both the direct documents and template reference model, along with additional options. This model provides the option to directly specify a document, to apply one or more server templates, and to provide additional details inline within a single envelope.
Advantage: The composite templates model supports any use case that the simpler models can address, as well as some situations that they can't handle. Even for basic use cases, creating an integration with a composite template builds in the flexibility to easily expand or enhance the solution later on without needing to rewrite it from the ground up.
Drawback: Implementing the composite templates model can require planning and troubleshooting, which can be a challenge to incorporate into a tight schedule.
Note: The composite templates model is built around an array of objects in the API request body. Each object in the array can directly specify a document, apply one or more envelope templates, and provide additional details inline. An object in this array is referred to as a template object. However, this is a separate concept from an envelope template that you create in the Docusign app. The template objects that make up the structure of the composite template model are created only within the body of an API call.
The following code shows the JSON body for a create envelope request using the composite templates model:
Choosing an Envelope Model
Direct documents: For a basic integration that doesn't require a template, using this approach can allow you to code up and deploy a solution quickly.
Template reference: When your requirements call for only a single template, using this model enables you to build a straightforward solution in with minimal coding.
Composite templates: When neither of the more basic approaches can meet the needs of your project, then this model is the obvious choice. In addition, if your organization is planning to grow your use of Docusign eSignature moving forward, then choosing the composite templates approach for more basic needs ensures that you'll have the architecture in place to scale and modify your integration in the future as your requirements change.
Lesson 2 - Construct an eSignature REST API Call to Create an Envelope

Build Envelopes and Use Templates with the eSignature API
Envelope Concepts and Models
Construct an eSignature REST API Call to Create an Envelope
DIRECT DOCUMENTS MODEL
Create Requests for the Direct Documents Model
TEMPLATE REFERENCE MODEL
Create Requests for the Template Reference Model
COMPOSITE TEMPLATES MODEL
Create Requests for the Composite Templates Model
ACTIVITY
Activity: Create Envelopes with API Calls
Envelope Concepts and Models
Objective: After reviewing this topic, you’ll be able to describe the components of an eSignature envelope and the envelope types that the eSignature API supports.
Docusign eSignature envelopes are built using a set of basic objects. You can combine these objects to build envelopes using the Docusign eSignature API based on a few different envelope models.
Envelope Concepts
Envelope Objects
Every agreement you send with Docusign eSignature is made up of four objects: envelope, document, recipient, and tab.
Envelope
Document
A document is a digital file whose content must be reviewed, signed, approved, or initialed by one or more recipients.
Documents can be uploaded from a device or added from a cloud storage system.
Docusign accepts a wide variety of document types, including PDF, DOCX, RTF, and PNG.
You can include multiple documents in a single envelope.
Documents are always encrypted while stored in the system.
Recipient
A recipient object represents a party receiving an envelope object.
Depending on their settings, recipients can sign the documents, add information indicated by tabs, or just view the envelope contents.
Tab
Envelope Templates
An envelope template is a preconfigured envelope structure you configure with documents, recipient roles, and tabs, and then reuse when you need to complete the same agreement process with different recipients.
The Docusign app is the easiest way to create and configure an envelope template. However, after you have created and saved a template to your account, you can reference it in API calls to build and send envelopes.
Document Generation Templates
A document generation template is a specialized envelope template where traditional field data is embedded seamlessly into the agreement. Document information is dynamically populated, generating final documents that are professional-looking and well formatted. A document generation template can also include conditional logic to show or hide sections based on the data supplied for a specific transaction.
Document generation templates are created and managed separately from standard envelope templates in the Docusign app. However, you can incorporate both of these types of envelope templates in eSignature API requests to build and send envelopes.
Envelope Models
When you build an envelope using the Docusign eSignature REST API, you have a few models to choose from for your envelope structure:
Direct documents model
Template reference model
Composite templates model
Direct Documents Model
Using the direct documents model, you build an envelope entirely from scratch in an API call, providing documents, recipients, and tabs within your request.
Advantage: When your integration has only basic needs, this type of solution can be quick to build.
Drawback: Because this approach uses no templates, the resulting envelope is not very flexible, and can require significant work to expand or replace as the needs of your integration change and grow.
The following code shows the JSON body for a create envelope request using the direct documents model:
Template Reference Model
When your API call uses the template reference model, you reference a single envelope template built in the Docusign app.
Advantage: This approach enables you to create an envelope using a single envelope template, which can be useful for a basic use case.
Drawback: An envelope using this model cannot be expanded to use multiple envelope templates, so it does not provide flexibility as the needs of your users grow.
The following code shows the JSON body for a create envelope request using the template reference model:
Composite Templates Model
An envelope built using the composite templates model supports the features of both the direct documents and template reference model, along with additional options. This model provides the option to directly specify a document, to apply one or more server templates, and to provide additional details inline within a single envelope.
Advantage: The composite templates model supports any use case that the simpler models can address, as well as some situations that they can't handle. Even for basic use cases, creating an integration with a composite template builds in the flexibility to easily expand or enhance the solution later on without needing to rewrite it from the ground up.
Drawback: Implementing the composite templates model can require planning and troubleshooting, which can be a challenge to incorporate into a tight schedule.
Note: The composite templates model is built around an array of objects in the API request body. Each object in the array can directly specify a document, apply one or more envelope templates, and provide additional details inline. An object in this array is referred to as a template object. However, this is a separate concept from an envelope template that you create in the Docusign app. The template objects that make up the structure of the composite template model are created only within the body of an API call.
The following code shows the JSON body for a create envelope request using the composite templates model:
Choosing an Envelope Model
Direct documents: For a basic integration that doesn't require a template, using this approach can allow you to code up and deploy a solution quickly.
Template reference: When your requirements call for only a single template, using this model enables you to build a straightforward solution in with minimal coding.
Composite templates: When neither of the more basic approaches can meet the needs of your project, then this model is the obvious choice. In addition, if your organization is planning to grow your use of Docusign eSignature moving forward, then choosing the composite templates approach for more basic needs ensures that you'll have the architecture in place to scale and modify your integration in the future as your requirements change.
Lesson 2 - Construct an eSignature REST API Call to Create an Envelope

Build Envelopes and Use Templates with the eSignature API
Envelope Concepts and Models
Construct an eSignature REST API Call to Create an Envelope
DIRECT DOCUMENTS MODEL
Create Requests for the Direct Documents Model
TEMPLATE REFERENCE MODEL
Create Requests for the Template Reference Model
COMPOSITE TEMPLATES MODEL
Create Requests for the Composite Templates Model
ACTIVITY
Activity: Create Envelopes with API Calls
Envelope Concepts and Models
Objective: After reviewing this topic, you’ll be able to describe the components of an eSignature envelope and the envelope types that the eSignature API supports.
Docusign eSignature envelopes are built using a set of basic objects. You can combine these objects to build envelopes using the Docusign eSignature API based on a few different envelope models.
Envelope Concepts
Envelope Objects
Every agreement you send with Docusign eSignature is made up of four objects: envelope, document, recipient, and tab.
Envelope
Document
A document is a digital file whose content must be reviewed, signed, approved, or initialed by one or more recipients.
Documents can be uploaded from a device or added from a cloud storage system.
Docusign accepts a wide variety of document types, including PDF, DOCX, RTF, and PNG.
You can include multiple documents in a single envelope.
Documents are always encrypted while stored in the system.
Recipient
A recipient object represents a party receiving an envelope object.
Depending on their settings, recipients can sign the documents, add information indicated by tabs, or just view the envelope contents.
Tab
A tab represents a Docusign field on a document.
Tabs are represented graphically as symbols on documents at the time of signing.
Tabs indicate to the recipient where to sign, initial, or enter data, or they show data to the recipient.
Envelope Templates
An envelope template is a preconfigured envelope structure you configure with documents, recipient roles, and tabs, and then reuse when you need to complete the same agreement process with different recipients.
The Docusign app is the easiest way to create and configure an envelope template. However, after you have created and saved a template to your account, you can reference it in API calls to build and send envelopes.
Document Generation Templates
A document generation template is a specialized envelope template where traditional field data is embedded seamlessly into the agreement. Document information is dynamically populated, generating final documents that are professional-looking and well formatted. A document generation template can also include conditional logic to show or hide sections based on the data supplied for a specific transaction.
Document generation templates are created and managed separately from standard envelope templates in the Docusign app. However, you can incorporate both of these types of envelope templates in eSignature API requests to build and send envelopes.
Envelope Models
When you build an envelope using the Docusign eSignature REST API, you have a few models to choose from for your envelope structure:
Direct documents model
Template reference model
Composite templates model
Direct Documents Model
Using the direct documents model, you build an envelope entirely from scratch in an API call, providing documents, recipients, and tabs within your request.
Advantage: When your integration has only basic needs, this type of solution can be quick to build.
Drawback: Because this approach uses no templates, the resulting envelope is not very flexible, and can require significant work to expand or replace as the needs of your integration change and grow.
The following code shows the JSON body for a create envelope request using the direct documents model:
Template Reference Model
When your API call uses the template reference model, you reference a single envelope template built in the Docusign app.
Advantage: This approach enables you to create an envelope using a single envelope template, which can be useful for a basic use case.
Drawback: An envelope using this model cannot be expanded to use multiple envelope templates, so it does not provide flexibility as the needs of your users grow.
The following code shows the JSON body for a create envelope request using the template reference model:
Composite Templates Model
An envelope built using the composite templates model supports the features of both the direct documents and template reference model, along with additional options. This model provides the option to directly specify a document, to apply one or more server templates, and to provide additional details inline within a single envelope.
Advantage: The composite templates model supports any use case that the simpler models can address, as well as some situations that they can't handle. Even for basic use cases, creating an integration with a composite template builds in the flexibility to easily expand or enhance the solution later on without needing to rewrite it from the ground up.
Drawback: Implementing the composite templates model can require planning and troubleshooting, which can be a challenge to incorporate into a tight schedule.
Note: The composite templates model is built around an array of objects in the API request body. Each object in the array can directly specify a document, apply one or more envelope templates, and provide additional details inline. An object in this array is referred to as a template object. However, this is a separate concept from an envelope template that you create in the Docusign app. The template objects that make up the structure of the composite template model are created only within the body of an API call.
The following code shows the JSON body for a create envelope request using the composite templates model:
Choosing an Envelope Model
Direct documents: For a basic integration that doesn't require a template, using this approach can allow you to code up and deploy a solution quickly.
Template reference: When your requirements call for only a single template, using this model enables you to build a straightforward solution in with minimal coding.
Composite templates: When neither of the more basic approaches can meet the needs of your project, then this model is the obvious choice. In addition, if your organization is planning to grow your use of Docusign eSignature moving forward, then choosing the composite templates approach for more basic needs ensures that you'll have the architecture in place to scale and modify your integration in the future as your requirements change.
Lesson 2 - Construct an eSignature REST API Call to Create an Envelope

Build Envelopes and Use Templates with the eSignature API
Envelope Concepts and Models
Construct an eSignature REST API Call to Create an Envelope
DIRECT DOCUMENTS MODEL
Create Requests for the Direct Documents Model
TEMPLATE REFERENCE MODEL
Create Requests for the Template Reference Model
COMPOSITE TEMPLATES MODEL
Create Requests for the Composite Templates Model
ACTIVITY
Activity: Create Envelopes with API Calls
Construct an eSignature REST API Call to Create an Envelope
Objective: After reviewing this topic, you will be able to build a call to the eSignature REST API to create an envelope.
Base URI
You request user information from the Envelopes: create endpoint
at the following path:
{baseUri}/{apiVersion}/accounts/{accountId}/envelopes
Like other URIs for other Docusign endpoints, the base URI for creating an envelope varies depending on whether your app is in development or is deployed to production:
Development
https://demo.docusign.net/restapi
Production
https://{site}.docusign.net/restapi
where {site} is the Docusign site that hosts your account, such as na3, eu, or au
Note:
All examples in this course use development endpoints. When deploying your app to production, ensure that you update all instances of the URI to use production endpoints.
The accountId parameter is the Docusign account ID for the account making the API call, which varies between development and production accounts. To programmatically retrieve this value, you call the oauth/userinfo endpoint after completing a supported OAuth flow.
Note: To learn about the OAuth flows supported by Docusign and how to integrate them into your app, enroll in the "Implement Authentication with Docusign APIs" self-paced learning plan in Docusign University.
JSON Body
The required JSON body properties to create an envelope vary depending on whether you are using the direct documents, template reference, or composite template model. You will review each of these JSON structures and their properties later in this course.
Required Headers
A request to create an envelope must include two required headers:
AUTHORIZATION
CONTENT-TYPE
The Authorization header value must include the word Bearer followed by a valid access token obtained using an OAuth2 flow.
Request
To create an envelope, you make a POST request to the Envelopes: create endpoint
with the JSON body and the headers.
Response
The returned response supplies you with an envelopeId value for the newly created envelope, along with a URI snippet for the envelope, the envelope status, and a time stamp.
Envelope Concepts and Models
Objective: After reviewing this topic, you’ll be able to describe the components of an eSignature envelope and the envelope types that the eSignature API supports.
Docusign eSignature envelopes are built using a set of basic objects. You can combine these objects to build envelopes using the Docusign eSignature API based on a few different envelope models.
Envelope Concepts
Envelope Objects
Every agreement you send with Docusign eSignature is made up of four objects: envelope, document, recipient, and tab.
Envelope
Document
A document is a digital file whose content must be reviewed, signed, approved, or initialed by one or more recipients.
Documents can be uploaded from a device or added from a cloud storage system.
Docusign accepts a wide variety of document types, including PDF, DOCX, RTF, and PNG.
You can include multiple documents in a single envelope.
Documents are always encrypted while stored in the system.
Recipient
A recipient object represents a party receiving an envelope object.
Depending on their settings, recipients can sign the documents, add information indicated by tabs, or just view the envelope contents.
Tab
A tab represents a Docusign field on a document.
Tabs are represented graphically as symbols on documents at the time of signing.
Tabs indicate to the recipient where to sign, initial, or enter data, or they show data to the recipient.
Envelope Templates
An envelope template is a preconfigured envelope structure you configure with documents, recipient roles, and tabs, and then reuse when you need to complete the same agreement process with different recipients.
The Docusign app is the easiest way to create and configure an envelope template. However, after you have created and saved a template to your account, you can reference it in API calls to build and send envelopes.
Document Generation Templates
A document generation template is a specialized envelope template where traditional field data is embedded seamlessly into the agreement. Document information is dynamically populated, generating final documents that are professional-looking and well formatted. A document generation template can also include conditional logic to show or hide sections based on the data supplied for a specific transaction.
Document generation templates are created and managed separately from standard envelope templates in the Docusign app. However, you can incorporate both of these types of envelope templates in eSignature API requests to build and send envelopes.
Envelope Models
When you build an envelope using the Docusign eSignature REST API, you have a few models to choose from for your envelope structure:
Direct documents model
Template reference model
Composite templates model
Direct Documents Model
Using the direct documents model, you build an envelope entirely from scratch in an API call, providing documents, recipients, and tabs within your request.
Advantage: When your integration has only basic needs, this type of solution can be quick to build.
Drawback: Because this approach uses no templates, the resulting envelope is not very flexible, and can require significant work to expand or replace as the needs of your integration change and grow.
The following code shows the JSON body for a create envelope request using the direct documents model:
Template Reference Model
When your API call uses the template reference model, you reference a single envelope template built in the Docusign app.
Advantage: This approach enables you to create an envelope using a single envelope template, which can be useful for a basic use case.
Drawback: An envelope using this model cannot be expanded to use multiple envelope templates, so it does not provide flexibility as the needs of your users grow.
The following code shows the JSON body for a create envelope request using the template reference model:
Composite Templates Model
An envelope built using the composite templates model supports the features of both the direct documents and template reference model, along with additional options. This model provides the option to directly specify a document, to apply one or more server templates, and to provide additional details inline within a single envelope.
Advantage: The composite templates model supports any use case that the simpler models can address, as well as some situations that they can't handle. Even for basic use cases, creating an integration with a composite template builds in the flexibility to easily expand or enhance the solution later on without needing to rewrite it from the ground up.
Drawback: Implementing the composite templates model can require planning and troubleshooting, which can be a challenge to incorporate into a tight schedule.
Note: The composite templates model is built around an array of objects in the API request body. Each object in the array can directly specify a document, apply one or more envelope templates, and provide additional details inline. An object in this array is referred to as a template object. However, this is a separate concept from an envelope template that you create in the Docusign app. The template objects that make up the structure of the composite template model are created only within the body of an API call.
The following code shows the JSON body for a create envelope request using the composite templates model:
Choosing an Envelope Model
Direct documents: For a basic integration that doesn't require a template, using this approach can allow you to code up and deploy a solution quickly.
Template reference: When your requirements call for only a single template, using this model enables you to build a straightforward solution in with minimal coding.
Composite templates: When neither of the more basic approaches can meet the needs of your project, then this model is the obvious choice. In addition, if your organization is planning to grow your use of Docusign eSignature moving forward, then choosing the composite templates approach for more basic needs ensures that you'll have the architecture in place to scale and modify your integration in the future as your requirements change.
Lesson 3 - Create Requests for the Direct Documents Model

Build Envelopes and Use Templates with the eSignature API
Envelope Concepts and Models
Construct an eSignature REST API Call to Create an Envelope
DIRECT DOCUMENTS MODEL
Create Requests for the Direct Documents Model
TEMPLATE REFERENCE MODEL
Create Requests for the Template Reference Model
COMPOSITE TEMPLATES MODEL
Create Requests for the Composite Templates Model
ACTIVITY
Activity: Create Envelopes with API Calls
Lesson 2 - Construct an eSignature REST API Call to Create an Envelope
Create Requests for the Direct Documents Model
Objective: After reviewing this topic, you will be able to build the JSON body for a call to the eSignature REST API using the direct documents model.
Required JSON body properties
A request to create an envelope using the direct documents model includes values for four required JSON body properties:
EMAILSUBJECT
DOCUMENTS
RECIPIENTS
STATUS
The emailSubject property specifies a subject for the notification email sent to envelope recipients.
Request
To create an envelope with the direct documents model, you make a POST request to the Envelopes: create endpoint
with the JSON body and the headers.
The snippets below show a raw HTTP request to create an envelope with direct documents, as well as code for building the same request in the cURL utility and in several commonly used programming languages.
HTTP
CURL
C#
NODE.JS REQUEST
PYTHON
RUBY
To include documents in the request, you create a multipart JSON request body that includes the document bytes. Use can use a Docusign eSignature REST API SDK to build this request, or review detailed steps by selecting the following button.
How to attach documents via binary transfer
Select the button to review a detailed explanation in the Docusign Developer Center on directly attaching documents to an envelope.
HOW TO
After your request is received, the API request is authenticated against the associated Docusign accountId, then the envelope is created, the documents, recipients, and tabs are applied, and the envelope is sent to all recipients in the specified routing order.
Lesson 4 - Create Requests for the Template Reference Model

Build Envelopes and Use Templates with the eSignature API
Envelope Concepts and Models
Construct an eSignature REST API Call to Create an Envelope
DIRECT DOCUMENTS MODEL
Create Requests for the Direct Documents Model
TEMPLATE REFERENCE MODEL
Create Requests for the Template Reference Model
COMPOSITE TEMPLATES MODEL
Create Requests for the Composite Templates Model
ACTIVITY
Activity: Create Envelopes with API Calls
Create Requests for the Template Reference Model
Objective: After reviewing this topic, you will be able to build the JSON body for a call to the eSignature REST API using the template reference model.
When you create an API request using the template reference model, you can include a single template. Docusign offers two main types of eSignature templates: standard envelope templates and document generation templates.
Standard envelope templates
Document generation templates
The process for creating and sending an envelope with the API is different depending on which template type you use.
Note: To learn about the advantages of each template type and how to create them, enroll in the Create Docusign Templates to Simplify Sending course at Docusign University.
Best Practice
Templates are typically set up once and then referenced, and Docusign recommends doing this initial setup in the Docusign eSignature app for each template, then referencing templates by ID in your API calls as needed. Although it is possible to create a template using an API call, it can be cumbersome to place Docusign tags within a document programmatically.
To send an envelope using a standard envelope template or a document generation template, you make a POST request to the Envelopes: create endpoint
, passing the template ID and other required properties.
Required JSON body properties
A request to create an envelope using a template includes values for three required JSON body properties:
STATUS
TEMPLATEID
TEMPLATEROLES
The status property specifies the initial envelope status, which is either "created" or "sent".
When using the "created" status, the envelope is not sent to recipients, and remains in a draft stage until the status is set to "sent".
When using the "sent" status, the envelope is created and immediately sent to all attached recipients in their defined routing order.
Note: To send with a document generation template, the first step is to create a draft envelope using a status of "created." You then use additional requests to add document generation field values to the envelope before changing the status to "sent."
You can retrieve the value for templateId by opening the template in the Docusign app and clicking the copy icon next to the template ID value.
You can also get this value by making an API request to the Templates: list endpoint
Note: Template ID values are different between developer and production accounts, so be sure to update these values as part of the go-live process for your integration.
Send with a Standard Envelope Template
To send an envelope with a standard envelope template, you simply make a POST request to the Envelopes: create
endpoint with the JSON body and the headers.
After your request is received, the envelope is authenticated against the associated Docusign accountId, then the envelope is created, the template is applied, and the envelope is sent to all recipients in the routing order defined by the template.
Send with a Document Generation Template
The process to send an envelope with a document generation template includes four main steps:
1
Create a draft envelope
2
Retrieve placeholder fields
3
Populate field values
4
Send the envelope
Create a draft envelope
To create an envelope definition from a document generation template, you make a POST request to the Envelopes: create
endpoint. You must specify values for templateId, templateRoles, and status, and the status value must be created.
Retrieve placeholder fields
To retrieve a list of the placeholder fields available on the template, you make a GET request to the DocumentGeneration: getEnvelopeDocGenFormFields
endpoint:
/restapi/v2.1/accounts/{accountId}/envelopes/{envelopeId}/docGenFormFields
The response includes all the fields available on your document including their label, type, required vs optional property, and name, as well as the document id.
The following JSON code shows example response data:
{
"docGenFormFields": [
{
"documentId": "b83617f9-xxxx-xxxx-xxxx-d5dda0ba77e6",
"docGenFormFieldList": [
{
"label": "Candidate_Name",
"type": "TextBox",
"required": "True",
"name": "Candidate_Name"
},
{
"label": "Job_Title",
"type": "TextBox",
"required": "True",
"name": "Job_Title"
},
{
"label": "Start_Date",
"type": "TextBox",
"required": "True",
"name": "Start_Date"
},
{
"label": "Annual_Salary",
"type": "TextBox",
"required": "True",
"name": "Annual_Salary"
}
],
"docGenDocumentStatus": "created"
}
]
}
Note: If your template contains a dynamic table, the response will include a rowValues.docGenFormFieldList array. This array defines the sender fields that make up the table row definition. For more information review the Developer Center guide
Populate field values
To populate the template fields with values, you make a PUT request to the DocumentGeneration: updateEnvelopeDocGenFormFields
endpoint:
/restapi/v2.1/accounts/{accountId}/envelopes/{envelopeId}/docGenFormFields
Your request body must reference the field names returned in the response to the previous request, and must provide a value for each required field.
The following JSON code shows an example request body:
{
"docGenFormFields": [
{
"documentId": "667017ec-xxxx-xxxx-xxxx-f1cc1a8fc11d",
"docGenFormFieldList": [
{
"name": "Candidate_Name",
"value": "Caroline Miller"
},
{
"name": "Job_Title",
"value": "Software Engineer"
},
{
"name": "Start_Date",
"value": "07/10/2023"
},
{
"name": "Annual_Salary",
"value": "$120,000"
}
],
"docGenDocumentStatus": "created"
}
]
}
If your document generation file includes conditional content, it will be applied during this step.
Send the envelope
To send the draft envelope for signature, you make a PUT request to the Envelopes: update
endpoint and set the "status" to "sent":
/restapi/v2.1/accounts/{accountId}/envelopes/{envelopeId}
{
"status": "sent"
}
After your request is received, the envelope is sent to all recipients in the routing order defined by the template.
Create Requests for the Direct Documents Model
Objective: After reviewing this topic, you will be able to build the JSON body for a call to the eSignature REST API using the direct documents model.
Required JSON body properties
A request to create an envelope using the direct documents model includes values for four required JSON body properties:
EMAILSUBJECT
DOCUMENTS
RECIPIENTS
STATUS
The emailSubject property specifies a subject for the notification email sent to envelope recipients.
Request
To create an envelope with the direct documents model, you make a POST request to the Envelopes: create endpoint
with the JSON body and the headers.
The snippets below show a raw HTTP request to create an envelope with direct documents, as well as code for building the same request in the cURL utility and in several commonly used programming languages.
HTTP
CURL
C#
NODE.JS REQUEST
PYTHON
RUBY
To include documents in the request, you create a multipart JSON request body that includes the document bytes. Use can use a Docusign eSignature REST API SDK to build this request, or review detailed steps by selecting the following button.
How to attach documents via binary transfer
Select the button to review a detailed explanation in the Docusign Developer Center on directly attaching documents to an envelope.
HOW TO
After your request is received, the API request is authenticated against the associated Docusign accountId, then the envelope is created, the documents, recipients, and tabs are applied, and the envelope is sent to all recipients in the specified routing order.
Lesson 5 - Create Requests for the Composite Templates Model

Build Envelopes and Use Templates with the eSignature API
Envelope Concepts and Models
Construct an eSignature REST API Call to Create an Envelope
DIRECT DOCUMENTS MODEL
Create Requests for the Direct Documents Model
TEMPLATE REFERENCE MODEL
Create Requests for the Template Reference Model
COMPOSITE TEMPLATES MODEL
Create Requests for the Composite Templates Model
ACTIVITY
Activity: Create Envelopes with API Calls
Create Requests for the Composite Templates Model
Objective: After reviewing this topic, you will be able to plan and structure an envelope using composite templates to fit your use case.
Building an envelope using a composite template structure involves multiple levels of nested objects and arrays, so we'll dig down one level at a time.
At the envelope level, the JSON body requires the compositeTemplates property, and commonly includes two other properties: emailSubject and status.
COMPOSITETEMPLATES
EMAILSUBJECT
STATUS
The compositeTemplates property specifies an array of one or more composite template objects to add to the envelope.
Structure of a Single Composite Template Object
The value of the compositeTemplates property is an array of objects. Each object in the array contains one composite template. A single envelope can include one or more composite template objects in the compositeTemplates array.
Within each composite template object, you add envelope content using one or more of the document, serverTemplates, and inlineTemplates properties.
DOCUMENT
SERVERTEMPLATES
INLINETEMPLATES
The optional document property specifies one direct document. If the document property is included, the direct document takes precedence over any server template or inline template documents. This option is generally only necessary when you need to supply the document dynamically.
Composite Template Structures for Different Requirements
The composite template structure supports any type of envelope content, including direct document and server template reference scenarios. While either of these types of envelopes can be created without composite templates, using the composite template model results in an envelope structure that's easier to modify and scale in the future. Implementing a composite template structure also unlocks capabilities that aren't available with the other two models.
Creating a Composite Template Structure for a Direct Document
To build a request using composite templates based only on directly supplied documents, you use a separate composite template object for each document. Within each composite template object, you use the document property to provide a document and related information, and you use the inlineTemplates property to add additional information for that document, such as recipients and tabs.
For example, the following code uses a single composite template object. The document property provides a document directly, and the inlineTemplates property adds recipient information.
Creating a Composite Template Structure for a Template Reference
To build a request using composite templates based only on documents from a single server template, you use a composite template object to reference the server template. You use the serverTemplates property to specify information about the server template, and you use the inlineTemplates property to add additional information to the envelope, such as recipients and tabs.
For example, the following code uses a single composite template object. The serverTemplates property specifies information about the server template, and the inlineTemplates property adds recipient information.
Leveraging the Unique Features of the Composite Template Structure
Composite templates enable you to build envelope structures that you can't create with other envelope models. Only composite templates support the following:
Applying multiple server templates in a single envelope per API call.
Applying multiple instances of same server template, and assigning different recipients to the same template role per instance.
Applying a server template to as many documents as you would like in your API call, either in addition to existing server template documents or by adding a new document to the template dynamically.
Extending the structure of a server template dynamically using inline templates.
For instance, the following code starts with a single directly supplied document, and then uses a single server template twice in the same API call, associating each instance with a different recipient. The resulting envelope is composed of the additional document plus two copies of the document from the server template, and each is built from a separate object within the composite template array.
Prioritizing Composite Template Documents, Attributes, and Objects
When building an envelope using composite templates, it is vital to understand and plan how the different components will fit together. This will help you ensure that the resulting envelope contains the documents and attributes you expect in the order you want. In particular, it is important to understand how documents, attributes, and composite template objects themselves are prioritized and ordered within an envelope.
Document Priority: First in Wins
Only one document can be contributed to each composite template object. Choosing the document is a multi-step process where the sequence property value can come into play. Every serverTemplate object and inlineTemplate object must have a sequence property, and sequence values must be unique within a composite template object. A best practice is to start sequence numbering from 1 within each individual composite template object.
Sequence values are not the only factor in determining document contribution within a composite template object, though. If multiple components supply documents, the document is chosen as follows:
1
Document element: If the composite template object includes a document element, the document supplied by this element is contributed to the object and any other documents are ignored.
2
Lowest sequence value: If no document element exists, then server templates and inline templates are examined in order of sequence value. The template with the lowest sequence value that supplies a document will be used for that composite template object, and any other documents supplied by templates higher in the sequence order are ignored.
In the code below, the doc_1.pdf document is contributed to the envelope and the document supplied by the server template is ignored, because the document property always takes priority for document contribution.
Note:
Although an inline template can contribute documents via its documents property, the best practice is to instead use the document property of the composite template object.
Attribute Priority: Last in Wins
serverTemplates and inlineTemplates values can contribute attributes to an envelope, such as recipients and tabs. Both types of templates are examined in order of their sequence values, but unlike documents, attributes with higher sequence values overwrite those with lower sequence values. For this reason, it is important to be intentional about the sequence order of templates within an object.
For example, if a server template specifies a recipient role and an inline template maps a recipient to that role name, it is essential that the server template have a lower sequence number than the inline template so that the role and associated tabs are established before a recipient is mapped to it.
In the code below, the server template with a sequence value of 1 is applied to the envelope before the inline template, whose sequence value is 2. This ensures that the composite template contains a document with a roleName of "customer" before a recipient is specified for this role.
If the sequence values were reversed and the inline template had a sequence value of 1 while the server template had a sequence value of 2, the roleName of "customer" specified by the inline template would not exist yet when it was applied to the composite template object.
Composite Template Object Order: Order in Array
In an envelope built from multiple composite template objects, the order of documents in the envelope is determined by the order of objects within the compositeTemplates array. The document in the first composite template object is displayed first, followed by the document in the next composite template object, and so on.
In the code below, the compositeTemplates array contains two composite template objects. The first object contains the CoverLetter document, and the second contains the document contributed by the server template. The document order in the envelope will follow the order in the array: CoverLetter first, followed by the server template document.
Create Requests for the Template Reference Model
Objective: After reviewing this topic, you will be able to build the JSON body for a call to the eSignature REST API using the template reference model.
When you create an API request using the template reference model, you can include a single template. Docusign offers two main types of eSignature templates: standard envelope templates and document generation templates.
Standard envelope templates
Document generation templates
The process for creating and sending an envelope with the API is different depending on which template type you use.
Note: To learn about the advantages of each template type and how to create them, enroll in the Create Docusign Templates to Simplify Sending course at Docusign University.
Best Practice
Templates are typically set up once and then referenced, and Docusign recommends doing this initial setup in the Docusign eSignature app for each template, then referencing templates by ID in your API calls as needed. Although it is possible to create a template using an API call, it can be cumbersome to place Docusign tags within a document programmatically.
To send an envelope using a standard envelope template or a document generation template, you make a POST request to the Envelopes: create endpoint
, passing the template ID and other required properties.
Required JSON body properties
A request to create an envelope using a template includes values for three required JSON body properties:
STATUS
TEMPLATEID
TEMPLATEROLES
The status property specifies the initial envelope status, which is either "created" or "sent".
When using the "created" status, the envelope is not sent to recipients, and remains in a draft stage until the status is set to "sent".
When using the "sent" status, the envelope is created and immediately sent to all attached recipients in their defined routing order.
Note: To send with a document generation template, the first step is to create a draft envelope using a status of "created." You then use additional requests to add document generation field values to the envelope before changing the status to "sent."
You can retrieve the value for templateId by opening the template in the Docusign app and clicking the copy icon next to the template ID value.
You can also get this value by making an API request to the Templates: list endpoint
Note: Template ID values are different between developer and production accounts, so be sure to update these values as part of the go-live process for your integration.
Send with a Standard Envelope Template
To send an envelope with a standard envelope template, you simply make a POST request to the Envelopes: create
endpoint with the JSON body and the headers.
After your request is received, the envelope is authenticated against the associated Docusign accountId, then the envelope is created, the template is applied, and the envelope is sent to all recipients in the routing order defined by the template.
Send with a Document Generation Template
The process to send an envelope with a document generation template includes four main steps:
1
Create a draft envelope
2
Retrieve placeholder fields
3
Populate field values
4
Send the envelope
Create a draft envelope
To create an envelope definition from a document generation template, you make a POST request to the Envelopes: create
endpoint. You must specify values for templateId, templateRoles, and status, and the status value must be created.
Retrieve placeholder fields
To retrieve a list of the placeholder fields available on the template, you make a GET request to the DocumentGeneration: getEnvelopeDocGenFormFields
endpoint:
/restapi/v2.1/accounts/{accountId}/envelopes/{envelopeId}/docGenFormFields
The response includes all the fields available on your document including their label, type, required vs optional property, and name, as well as the document id.
The following JSON code shows example response data:
{
"docGenFormFields": [
{
"documentId": "b83617f9-xxxx-xxxx-xxxx-d5dda0ba77e6",
"docGenFormFieldList": [
{
"label": "Candidate_Name",
"type": "TextBox",
"required": "True",
"name": "Candidate_Name"
},
{
"label": "Job_Title",
"type": "TextBox",
"required": "True",
"name": "Job_Title"
},
{
"label": "Start_Date",
"type": "TextBox",
"required": "True",
"name": "Start_Date"
},
{
"label": "Annual_Salary",
"type": "TextBox",
"required": "True",
"name": "Annual_Salary"
}
],
"docGenDocumentStatus": "created"
}
]
}
Note: If your template contains a dynamic table, the response will include a rowValues.docGenFormFieldList array. This array defines the sender fields that make up the table row definition. For more information review the Developer Center guide
Populate field values
To populate the template fields with values, you make a PUT request to the DocumentGeneration: updateEnvelopeDocGenFormFields
endpoint:
/restapi/v2.1/accounts/{accountId}/envelopes/{envelopeId}/docGenFormFields
Your request body must reference the field names returned in the response to the previous request, and must provide a value for each required field.
The following JSON code shows an example request body:
{
"docGenFormFields": [
{
"documentId": "667017ec-xxxx-xxxx-xxxx-f1cc1a8fc11d",
"docGenFormFieldList": [
{
"name": "Candidate_Name",
"value": "Caroline Miller"
},
{
"name": "Job_Title",
"value": "Software Engineer"
},
{
"name": "Start_Date",
"value": "07/10/2023"
},
{
"name": "Annual_Salary",
"value": "$120,000"
}
],
"docGenDocumentStatus": "created"
}
]
}
If your document generation file includes conditional content, it will be applied during this step.
Send the envelope
To send the draft envelope for signature, you make a PUT request to the Envelopes: update
endpoint and set the "status" to "sent":
/restapi/v2.1/accounts/{accountId}/envelopes/{envelopeId}
{
"status": "sent"
}
After your request is received, the envelope is sent to all recipients in the routing order defined by the template.
Lesson 6 - Activity: Create Envelopes with API Calls

### Bulk Send with the eSignature API 20 min

Bulk Send with the eSignature API
Introduction to Bulk Send
Prepare a Bulk Envelope
Set up Bulk Status Notifications
Knowledge Check
Activity: Prepare and Send a Bulk Envelope
Lesson 4 - Knowledge Check
Activity: Prepare and Send a Bulk Envelope
Objective: After reviewing this topic, you will be able to create a draft bulk envelope and bulk list, and test, initiate, and check the status of a bulk send.
Let's walk through the process of creating and initiating a bulk send with the API. Follow the steps below to complete the activity. The steps are sequenced and must be completed in order. This activity can be completed in 10 minutes.
Setup
Before beginning this activity, be sure you have created a Docusign developer account.
Create a Bulk Send List
1
Click the CREATE BULK LIST button following this step to view the BulkSend: createBulkSendList method in the Docusign Developer Center API Explorer, then log in if necessary.
Docusign API Explorer: BulkSend: createBulkSendList
CREATE BULK LIST
2
Copy the following code to the clipboard:
Note: The preceding code box includes over 40 lines of code. Be sure to select all the lines of code before copying.
3
In the API Explorer, just after the Parameters section, click JSON Editor, then in the box that opens, delete the {} characters and paste the code you copied.
4
Change one or more of the email addresses in the code you pasted to addresses you control.
5
Click Get Response to send the request, then verify that the response includes a response code of 201 Created and the response body includes a value for the listId property.
Note: If the Get Response button is not visible, dismiss the Cookies Preferences bar at the bottom of the page.
6
In the response body, select and copy the value of the listId property, then paste the value into a separate file or note for use later in this activity.
Create a Draft Envelope
1
Click the CREATE ENVELOPE button following this step to view the Envelopes: create method in the Docusign Developer Center API Explorer.
Docusign API Explorer: Envelopes: create method
CREATE ENVELOPE
2
Copy the following code to the clipboard:
3
In the API Explorer, just after the Parameters section, click JSON Editor, then in the box that opens, delete the {} characters and paste the code you copied.
4
Click the Mutual_NDA.zip box following this step to download a ZIP file containing a template.
Mutual_NDA.zip
51.8 KB
5
In another browser tab, open https://apps-d.docusign.com/send
, then log into your Docusign developer account.
6
Click the Templates menu at the top of the page, click Start, click Upload Template, select the Mutual_NDA.zip file you just downloaded, then click Open.
7
On the My Templates list, click the Mutual NDA template, then on the page that opens, click the Template ID button and click COPY to copy the UUID for the template to the clipboard.
8
In the API Explorer, on line 9 of the code you pasted, paste the UUID you copied in place of the placeholder text.
9
Click Get Response to send the request, then verify that the response has a response code of 201 Created, and the response body includes a value for the envelopeId property.
10
In the response body, select and copy the value of the envelopeId property, then paste the value into a separate file or note for use later in this activity.
Test a Bulk Send
1
Click the CREATE BULK TEST button following this step to view the BulkSend: createBulkSendTestRequest method in the Docusign Developer Center API Explorer.
Docusign API Explorer: BulkSend: createBulkSendTestRequest
CREATE BULK TEST
2
Copy the listId value you obtained earlier in this activity, then in the API Explorer, within the Parameters section, paste the value in the bulkSendListId box.
3
Copy the envelopeId value you obtained earlier in this activity, then in the Body section, paste the value in the envelopeOrTemplateId box.
4
Click Get Response to send the request, then verify that the response includes a response code of 200 OK and the response body includes the canBeSent property with a value of true.
Initiate a Bulk Send
1
Click the CREATE REQUEST button following this step to view the BulkSend: createBulkSendRequest method in the Docusign Developer Center API Explorer.
Docusign API Explorer: BulkSend: createBulkSendRequest
CREATE REQUEST
2
Copy the bulkSendListId value you obtained earlier in this activity, then in the API Explorer, within the Parameters section, paste the value in the bulkSendListId box.
3
Copy the envelopeId value you obtained earlier in this activity, then in the Body section, paste the value in the envelopeOrTemplateId box.
4
Click Get Response to send the request, then verify that the response includes a response code of 201 Created and the response body includes a value for the batchId property.
5
In the response body, select and copy the value of the batchId property, then paste the value into a separate file or note for use later in this activity.
Check Bulk Send Status
1
Click the CHECK STATUS button following this step to view the BulkSend: getBulkSendBatchStatus method in the Docusign Developer Center API Explorer.
Docusign API Explorer: BulkSend: getBulkSendBatchStatus
CHECK STATUS
2
Copy the bulkSendBatchId value you obtained earlier in this activity, then in the API Explorer, within the Parameters section, paste the value in the bulkSendBatchId box.
3
Click Get Response to send the request, then verify that the response includes a response code of 200 OK.
4
In the response body, check the values for the sent, queued, and failed properties.
5
If the queued value is not 0, wait a few seconds, submit the request again, and repeat if necessary until the response body shows no more envelopes are queued.

Bulk Send with the eSignature API
Welcome to the Bulk Send with the eSignature API course. After reviewing this course, you will be able to send envelopes in bulk using the Docusign eSignature REST API, and test and monitor bulk envelopes.
Introduction to Bulk Send
Prepare a Bulk Envelope
Set up Bulk Status Notifications
Knowledge Check
Activity: Prepare and Send a Bulk Envelope

Bulk Send with the eSignature API
Introduction to Bulk Send
Prepare a Bulk Envelope
Set up Bulk Status Notifications
Knowledge Check
Activity: Prepare and Send a Bulk Envelope
Lesson 5 - Activity: Prepare and Send a Bulk Envelope
Docusign University
Continue learning about the topics covered in this course. Search Docusign University to explore recommended content listed below. Click the link for your account type to register. (Customer
| Developer/Demo
| Employee
| Partner
)
Trigger Actions with eSignature Data
Configure Docusign Connect Webhooks with the eSignature API
Best-practice Guide: Bulk Send Best Practices
Additional Resources
Docusign Support
Docusign Community
Docusign on YouTube
Docusign Developer Center
Docusign IAM
Create, commit to, and manage your agreements all in one collaborative platform.
What is Docusign IAM?
What can you do with Docusign IAM?
Visit the Docusign University IAM Learning Plans page to learn more about Docusign IAM. (Customers
| Developers
| Employees
| Partners
)
Docusign Certifications
Distinguish yourself as a Docusign expert by demonstrating your skills and experience with Docusign products and solutions.
Visit our certifications page or watch the video below to learn more about getting Docusign Certified. (Customers
| Developers
| Employees
| Partners
)
Lesson 7 - Course Complete

Bulk Send with the eSignature API
Introduction to Bulk Send
Prepare a Bulk Envelope
Set up Bulk Status Notifications
Knowledge Check
Activity: Prepare and Send a Bulk Envelope
Prepare a Bulk Envelope
Objective: After reviewing this topic, you will be able to build and send a bulk envelope.
Creating and sending bulk envelopes involves three main steps and two optional activities:
1
Create a bulk send list
2
Create a draft envelope
3
Test the bulk send (optional)
4
Initiate the bulk send
5
Check the bulk send status (optional)
Review each step to examine the bulk send process in more detail.
Create a Bulk Send List
Create a Draft Envelope
Test the Bulk Send (optional)
Initiate the Bulk Send
Check the Bulk Send Status (optional)
Note: The process outlined in this course uses v2.1 of the eSignature API, which changed the bulk send construction model. To learn more about the legacy API v2 bulk send workflow, see the API v2 BulkEnvelopes Resource
documentation in the Docusign Developer Center. To learn more about the legacy API v2 bulk send workflow, see the BulkEnvelopes Resource
documentation in the Docusign Developer Center and select REST API v2 in the version selector.
Executing a bulk send triggers the creation and sending of an individual envelope for each recipient in your list. Each recipient in your list gets their own agreement. All of the agreements are placed in a queue, and then agreements are pulled from the queue to be sent in cycles. The queue has a limit of 2000 envelopes. If the limit is reached, you will receive an error message. In that scenario, you must wait until there is adequate space allocated in the queue to send another bulk envelope.
Docusign University
Continue learning about the topics covered in this course. Search Docusign University to explore recommended content listed below. Click the link for your account type to register. (Customer
| Developer/Demo
| Employee
| Partner
)
Trigger Actions with eSignature Data
Configure Docusign Connect Webhooks with the eSignature API
Best-practice Guide: Bulk Send Best Practices
Additional Resources
Docusign Support
Docusign Community
Docusign on YouTube
Docusign Developer Center
Docusign IAM
Create, commit to, and manage your agreements all in one collaborative platform.
What is Docusign IAM?
What can you do with Docusign IAM?
Visit the Docusign University IAM Learning Plans page to learn more about Docusign IAM. (Customers
| Developers
| Employees
| Partners
)
Docusign Certifications
Distinguish yourself as a Docusign expert by demonstrating your skills and experience with Docusign products and solutions.
Visit our certifications page or watch the video below to learn more about getting Docusign Certified. (Customers
| Developers
| Employees
| Partners
)
Lesson 3 - Set up Bulk Status Notifications

Bulk Send with the eSignature API
Introduction to Bulk Send
Prepare a Bulk Envelope
Set up Bulk Status Notifications
Knowledge Check
Activity: Prepare and Send a Bulk Envelope
Set up Bulk Status Notifications
Objective: After reviewing this topic, you will be able to configure notifications for bulk envelope status.
Checking Bulk Send Status with Docusign Connect
The Docusign eSignature API limits the number of calls per hour. You can avoid making unnecessary API calls that would count against your limit by configuring push notifications instead. The Docusign Connect
service sends real-time data updates to external applications for any envelopes created in your Docusign account. Connect can be configured to send updates in response to several different envelope events and recipient actions.
Article: Docusign Connect (webhooks)
This article describes how Docusign Connect works and considerations for using it, including when to use it, Connect security, and events that can trigger Connect.
ARTICLE
Choosing a Docusign Connect Solution
Docusign Connect supports pre-built solutions for popular third-party services, as well as custom integrations. Pre-built solutions can be useful when you need to archive completed documents. A custom configuration may be the best choice if you need to integrate with an internal system for storage or to initiate additional steps after an envelope status changes.
Using Docusign Connect with a Pre-Built Third-Party Integration
Docusign supports pre-built integrations for Box, OneDrive, Salesforce, and eOriginal. The data that Docusign Connect pushes varies depending on the third-party service:
Connect for Box and Connect for OneDrive push completed documents to a Box or OneDrive folder, respectively.
Connect for Salesforce pushes data updates to the Docusign for Salesforce application.
Connect for eOriginal pushes an event to eOriginal informing the eOriginal system that a transaction that needs to be vaulted is complete.
Using Docusign Connect with a Custom Configuration
Creating a custom configuration to send events to your custom listener enables you to:
Store signed documents in an organization's storage system
Trigger additional business actions after the envelope has been completed. For example, initiate automatic provisioning or shipment after the contract has been signed.
Automatically update business data systems with data from the signed envelope. For example, if the signer updated their address as part of the signing process, you could start the process to update the signer's address in line-of-business applications.
Prepare a Bulk Envelope
Objective: After reviewing this topic, you will be able to build and send a bulk envelope.
Creating and sending bulk envelopes involves three main steps and two optional activities:
1
Create a bulk send list
2
Create a draft envelope
3
Test the bulk send (optional)
4
Initiate the bulk send
5
Check the bulk send status (optional)
Review each step to examine the bulk send process in more detail.
Create a Bulk Send List
Create a Draft Envelope
Test the Bulk Send (optional)
Initiate the Bulk Send
Check the Bulk Send Status (optional)
Note: The process outlined in this course uses v2.1 of the eSignature API, which changed the bulk send construction model. To learn more about the legacy API v2 bulk send workflow, see the API v2 BulkEnvelopes Resource
documentation in the Docusign Developer Center. To learn more about the legacy API v2 bulk send workflow, see the BulkEnvelopes Resource
documentation in the Docusign Developer Center and select REST API v2 in the version selector.
Executing a bulk send triggers the creation and sending of an individual envelope for each recipient in your list. Each recipient in your list gets their own agreement. All of the agreements are placed in a queue, and then agreements are pulled from the queue to be sent in cycles. The queue has a limit of 2000 envelopes. If the limit is reached, you will receive an error message. In that scenario, you must wait until there is adequate space allocated in the queue to send another bulk envelope.
Lesson 4 - Knowledge Check

Bulk Send with the eSignature API
Introduction to Bulk Send
Prepare a Bulk Envelope
Set up Bulk Status Notifications
Knowledge Check
Activity: Prepare and Send a Bulk Envelope
Knowledge Check
Which two steps in the bulk send process are optional? (Select TWO)
Create a draft envelope
Create a bulk send list
Test the bulk send
Initiate the bulk send
Check the bulk send status
SUBMIT
Incorrect
It's a good idea to test your bulk send before initiating it, but this step is not strictly required. After initiating your bulk send, you have the option of checking envelope status at any time, but the bulk send proceeds even if you don't check its status.
TAKE AGAIN
To ensure an envelope you create is a draft envelope, which value do you specify for the status property?
created
draft
sent
mock
SUBMIT
Incorrect
A status of created builds the envelope without sending it.
TAKE AGAIN
Match the value that's returned from each step in the bulk send process.
1
sent/queued/failed envelope counts
2
batchId
3
canBeSent (Boolean)
4
bulkListId
5
envelopeId
Create a Draft Envelope
Create a Bulk Send List
Test the Bulk Send
Initiate the Bulk Send
Check the Bulk Send
SUBMIT
Correct
Creating a draft envelope returns the envelopeId of the created envelope for use later in the process. Likewise, creating a bulk send list returns the bulkListId of the created list for later use. Testing a bulk send returns a Boolean value that indicates whether the submitted bulk send request can be sent. Initiating a bulk send returns a batchId that can be used to check the status of envelopes in the batch. Finally, checking a bulk send returns counts of sent, queued, and failed envelopes, as well as any error messages resulting from envelopes in the specified batch.
The bulk send queue has a limit of how many envelopes?
500
1000
2000
5000
SUBMIT
Incorrect
Large bulk send operations require advance planning and monitoring to avoid hitting your queue limit.
TAKE AGAIN
In this activity you will determine whether a use case presented could be solved by sending a single envelope or a bulk send envelope. Drag each use case example to either the Single Envelope box or the Bulk Envelope box.
0/6 Cards Correct
REPLAY
An offer letter that needs to be sent through HR, recruiters, and managers.
A company newsletter that needs to go out to a large subscriber base.
A CRM dataset containing lead email addresses for a marketing campaign
Complex flow with 5 documents, and a set number of people must act upon all 5.
Several documents for delivery to all employees at a partner company.
A single document where a fixed number of external parties need to sign.
Single Envelope
Bulk Envelope
Set up Bulk Status Notifications
Objective: After reviewing this topic, you will be able to configure notifications for bulk envelope status.
Checking Bulk Send Status with Docusign Connect
The Docusign eSignature API limits the number of calls per hour. You can avoid making unnecessary API calls that would count against your limit by configuring push notifications instead. The Docusign Connect
service sends real-time data updates to external applications for any envelopes created in your Docusign account. Connect can be configured to send updates in response to several different envelope events and recipient actions.
Article: Docusign Connect (webhooks)
This article describes how Docusign Connect works and considerations for using it, including when to use it, Connect security, and events that can trigger Connect.
ARTICLE
Choosing a Docusign Connect Solution
Docusign Connect supports pre-built solutions for popular third-party services, as well as custom integrations. Pre-built solutions can be useful when you need to archive completed documents. A custom configuration may be the best choice if you need to integrate with an internal system for storage or to initiate additional steps after an envelope status changes.
Using Docusign Connect with a Pre-Built Third-Party Integration
Docusign supports pre-built integrations for Box, OneDrive, Salesforce, and eOriginal. The data that Docusign Connect pushes varies depending on the third-party service:
Connect for Box and Connect for OneDrive push completed documents to a Box or OneDrive folder, respectively.
Connect for Salesforce pushes data updates to the Docusign for Salesforce application.
Connect for eOriginal pushes an event to eOriginal informing the eOriginal system that a transaction that needs to be vaulted is complete.
Using Docusign Connect with a Custom Configuration
Creating a custom configuration to send events to your custom listener enables you to:
Store signed documents in an organization's storage system
Trigger additional business actions after the envelope has been completed. For example, initiate automatic provisioning or shipment after the contract has been signed.
Automatically update business data systems with data from the signed envelope. For example, if the signer updated their address as part of the signing process, you could start the process to update the signer's address in line-of-business applications.
Lesson 5 - Activity: Prepare and Send a Bulk Envelope

Bulk Send with the eSignature API
Introduction to Bulk Send
Prepare a Bulk Envelope
Set up Bulk Status Notifications
Knowledge Check
Activity: Prepare and Send a Bulk Envelope
Objective: After reviewing this topic, you will be able to create a draft bulk envelope and bulk list, and test, initiate, and check the status of a bulk send.
Let's walk through the process of creating and initiating a bulk send with the API. Follow the steps below to complete the activity. The steps are sequenced and must be completed in order. This activity can be completed in 10 minutes.
Setup
Before beginning this activity, be sure you have created a Docusign developer account.
Create a Bulk Send List
1
Click the CREATE BULK LIST button following this step to view the BulkSend: createBulkSendList method in the Docusign Developer Center API Explorer, then log in if necessary.
Docusign API Explorer: BulkSend: createBulkSendList
CREATE BULK LIST
2
Copy the following code to the clipboard:
Note: The preceding code box includes over 40 lines of code. Be sure to select all the lines of code before copying.
3
In the API Explorer, just after the Parameters section, click JSON Editor, then in the box that opens, delete the {} characters and paste the code you copied.
4
Change one or more of the email addresses in the code you pasted to addresses you control.
5
Click Get Response to send the request, then verify that the response includes a response code of 201 Created and the response body includes a value for the listId property.
Note: If the Get Response button is not visible, dismiss the Cookies Preferences bar at the bottom of the page.
6
In the response body, select and copy the value of the listId property, then paste the value into a separate file or note for use later in this activity.
Create a Draft Envelope
1
Click the CREATE ENVELOPE button following this step to view the Envelopes: create method in the Docusign Developer Center API Explorer.
Docusign API Explorer: Envelopes: create method
CREATE ENVELOPE
2
Copy the following code to the clipboard:
3
In the API Explorer, just after the Parameters section, click JSON Editor, then in the box that opens, delete the {} characters and paste the code you copied.
4
Click the Mutual_NDA.zip box following this step to download a ZIP file containing a template.
Mutual_NDA.zip
51.8 KB
5
In another browser tab, open https://apps-d.docusign.com/send
, then log into your Docusign developer account.
6
Click the Templates menu at the top of the page, click Start, click Upload Template, select the Mutual_NDA.zip file you just downloaded, then click Open.
7
On the My Templates list, click the Mutual NDA template, then on the page that opens, click the Template ID button and click COPY to copy the UUID for the template to the clipboard.
8
In the API Explorer, on line 9 of the code you pasted, paste the UUID you copied in place of the placeholder text.
9
Click Get Response to send the request, then verify that the response has a response code of 201 Created, and the response body includes a value for the envelopeId property.
10
In the response body, select and copy the value of the envelopeId property, then paste the value into a separate file or note for use later in this activity.
Test a Bulk Send
1
Click the CREATE BULK TEST button following this step to view the BulkSend: createBulkSendTestRequest method in the Docusign Developer Center API Explorer.
Docusign API Explorer: BulkSend: createBulkSendTestRequest
CREATE BULK TEST
2
Copy the listId value you obtained earlier in this activity, then in the API Explorer, within the Parameters section, paste the value in the bulkSendListId box.
3
Copy the envelopeId value you obtained earlier in this activity, then in the Body section, paste the value in the envelopeOrTemplateId box.
4
Click Get Response to send the request, then verify that the response includes a response code of 200 OK and the response body includes the canBeSent property with a value of true.
Initiate a Bulk Send
1
Click the CREATE REQUEST button following this step to view the BulkSend: createBulkSendRequest method in the Docusign Developer Center API Explorer.
Docusign API Explorer: BulkSend: createBulkSendRequest
CREATE REQUEST
2
Copy the bulkSendListId value you obtained earlier in this activity, then in the API Explorer, within the Parameters section, paste the value in the bulkSendListId box.
3
Copy the envelopeId value you obtained earlier in this activity, then in the Body section, paste the value in the envelopeOrTemplateId box.
4
Click Get Response to send the request, then verify that the response includes a response code of 201 Created and the response body includes a value for the batchId property.
5
In the response body, select and copy the value of the batchId property, then paste the value into a separate file or note for use later in this activity.
Check Bulk Send Status
1
Click the CHECK STATUS button following this step to view the BulkSend: getBulkSendBatchStatus method in the Docusign Developer Center API Explorer.
Docusign API Explorer: BulkSend: getBulkSendBatchStatus
CHECK STATUS
2
Copy the bulkSendBatchId value you obtained earlier in this activity, then in the API Explorer, within the Parameters section, paste the value in the bulkSendBatchId box.
3
Click Get Response to send the request, then verify that the response includes a response code of 200 OK.
4
In the response body, check the values for the sent, queued, and failed properties.
5
If the queued value is not 0, wait a few seconds, submit the request again, and repeat if necessary until the response body shows no more envelopes are queued.
Knowledge Check
Which two steps in the bulk send process are optional? (Select TWO)
Create a draft envelope
Create a bulk send list
Test the bulk send
Initiate the bulk send
Check the bulk send status
SUBMIT
Incorrect
It's a good idea to test your bulk send before initiating it, but this step is not strictly required. After initiating your bulk send, you have the option of checking envelope status at any time, but the bulk send proceeds even if you don't check its status.
TAKE AGAIN
To ensure an envelope you create is a draft envelope, which value do you specify for the status property?
created
draft
sent
mock
SUBMIT
Incorrect
A status of created builds the envelope without sending it.
TAKE AGAIN
Match the value that's returned from each step in the bulk send process.
1
sent/queued/failed envelope counts
2
batchId
3
canBeSent (Boolean)
4
bulkListId
5
envelopeId
Create a Draft Envelope
Create a Bulk Send List
Test the Bulk Send
Initiate the Bulk Send
Check the Bulk Send
SUBMIT
Correct
Creating a draft envelope returns the envelopeId of the created envelope for use later in the process. Likewise, creating a bulk send list returns the bulkListId of the created list for later use. Testing a bulk send returns a Boolean value that indicates whether the submitted bulk send request can be sent. Initiating a bulk send returns a batchId that can be used to check the status of envelopes in the batch. Finally, checking a bulk send returns counts of sent, queued, and failed envelopes, as well as any error messages resulting from envelopes in the specified batch.
The bulk send queue has a limit of how many envelopes?
500
1000
2000
5000
SUBMIT
Incorrect
Large bulk send operations require advance planning and monitoring to avoid hitting your queue limit.
TAKE AGAIN
In this activity you will determine whether a use case presented could be solved by sending a single envelope or a bulk send envelope. Drag each use case example to either the Single Envelope box or the Bulk Envelope box.
0/6 Cards Correct
REPLAY
An offer letter that needs to be sent through HR, recruiters, and managers.
A company newsletter that needs to go out to a large subscriber base.
A CRM dataset containing lead email addresses for a marketing campaign
Complex flow with 5 documents, and a set number of people must act upon all 5.
Several documents for delivery to all employees at a partner company.
A single document where a fixed number of external parties need to sign.
Single Envelope
Bulk Envelope

Bulk Send with the eSignature API
Introduction to Bulk Send
Prepare a Bulk Envelope
Set up Bulk Status Notifications
Knowledge Check
Activity: Prepare and Send a Bulk Envelope
Knowledge Check
Which two steps in the bulk send process are optional? (Select TWO)
Create a draft envelope
Create a bulk send list
Test the bulk send
Initiate the bulk send
Check the bulk send status
SUBMIT
Incorrect
It's a good idea to test your bulk send before initiating it, but this step is not strictly required. After initiating your bulk send, you have the option of checking envelope status at any time, but the bulk send proceeds even if you don't check its status.
TAKE AGAIN
To ensure an envelope you create is a draft envelope, which value do you specify for the status property?
created
draft
sent
mock
SUBMIT
Incorrect
A status of created builds the envelope without sending it.
TAKE AGAIN
Match the value that's returned from each step in the bulk send process.
1
sent/queued/failed envelope counts
2
canBeSent (Boolean)
3
bulkListId
4
batchId
5
envelopeId
Create a Draft Envelope
Create a Bulk Send List
Test the Bulk Send
Initiate the Bulk Send
Check the Bulk Send
SUBMIT
Correct
Creating a draft envelope returns the envelopeId of the created envelope for use later in the process. Likewise, creating a bulk send list returns the bulkListId of the created list for later use. Testing a bulk send returns a Boolean value that indicates whether the submitted bulk send request can be sent. Initiating a bulk send returns a batchId that can be used to check the status of envelopes in the batch. Finally, checking a bulk send returns counts of sent, queued, and failed envelopes, as well as any error messages resulting from envelopes in the specified batch.
The bulk send queue has a limit of how many envelopes?
500
1000
2000
5000
SUBMIT
Incorrect
Large bulk send operations require advance planning and monitoring to avoid hitting your queue limit.
TAKE AGAIN
In this activity you will determine whether a use case presented could be solved by sending a single envelope or a bulk send envelope. Drag each use case example to either the Single Envelope box or the Bulk Envelope box.
0/6 Cards Correct
REPLAY
A CRM dataset containing lead email addresses for a marketing campaign
A single document where a fixed number of external parties need to sign.
Complex flow with 5 documents, and a set number of people must act upon all 5.
Several documents for delivery to all employees at a partner company.
An offer letter that needs to be sent through HR, recruiters, and managers.
A company newsletter that needs to go out to a large subscriber base.
Single Envelope
Bulk Envelope
Activity: Prepare and Send a Bulk Envelope
Objective: After reviewing this topic, you will be able to create a draft bulk envelope and bulk list, and test, initiate, and check the status of a bulk send.
Let's walk through the process of creating and initiating a bulk send with the API. Follow the steps below to complete the activity. The steps are sequenced and must be completed in order. This activity can be completed in 10 minutes.
Setup
Before beginning this activity, be sure you have created a Docusign developer account.
Create a Bulk Send List
1
Click the CREATE BULK LIST button following this step to view the BulkSend: createBulkSendList method in the Docusign Developer Center API Explorer, then log in if necessary.
Docusign API Explorer: BulkSend: createBulkSendList
CREATE BULK LIST
2
Copy the following code to the clipboard:
Note: The preceding code box includes over 40 lines of code. Be sure to select all the lines of code before copying.
3
In the API Explorer, just after the Parameters section, click JSON Editor, then in the box that opens, delete the {} characters and paste the code you copied.
4
Change one or more of the email addresses in the code you pasted to addresses you control.
5
Click Get Response to send the request, then verify that the response includes a response code of 201 Created and the response body includes a value for the listId property.
Note: If the Get Response button is not visible, dismiss the Cookies Preferences bar at the bottom of the page.
6
In the response body, select and copy the value of the listId property, then paste the value into a separate file or note for use later in this activity.
Create a Draft Envelope
1
Click the CREATE ENVELOPE button following this step to view the Envelopes: create method in the Docusign Developer Center API Explorer.
Docusign API Explorer: Envelopes: create method
CREATE ENVELOPE
2
Copy the following code to the clipboard:
3
In the API Explorer, just after the Parameters section, click JSON Editor, then in the box that opens, delete the {} characters and paste the code you copied.
4
Click the Mutual_NDA.zip box following this step to download a ZIP file containing a template.
Mutual_NDA.zip
51.8 KB
5
In another browser tab, open https://apps-d.docusign.com/send
, then log into your Docusign developer account.
6
Click the Templates menu at the top of the page, click Start, click Upload Template, select the Mutual_NDA.zip file you just downloaded, then click Open.
7
On the My Templates list, click the Mutual NDA template, then on the page that opens, click the Template ID button and click COPY to copy the UUID for the template to the clipboard.
8
In the API Explorer, on line 9 of the code you pasted, paste the UUID you copied in place of the placeholder text.
9
Click Get Response to send the request, then verify that the response has a response code of 201 Created, and the response body includes a value for the envelopeId property.
10
In the response body, select and copy the value of the envelopeId property, then paste the value into a separate file or note for use later in this activity.
Test a Bulk Send
1
Click the CREATE BULK TEST button following this step to view the BulkSend: createBulkSendTestRequest method in the Docusign Developer Center API Explorer.
Docusign API Explorer: BulkSend: createBulkSendTestRequest
CREATE BULK TEST
2
Copy the listId value you obtained earlier in this activity, then in the API Explorer, within the Parameters section, paste the value in the bulkSendListId box.
3
Copy the envelopeId value you obtained earlier in this activity, then in the Body section, paste the value in the envelopeOrTemplateId box.
4
Click Get Response to send the request, then verify that the response includes a response code of 200 OK and the response body includes the canBeSent property with a value of true.
Initiate a Bulk Send
1
Click the CREATE REQUEST button following this step to view the BulkSend: createBulkSendRequest method in the Docusign Developer Center API Explorer.
Docusign API Explorer: BulkSend: createBulkSendRequest
CREATE REQUEST
2
Copy the bulkSendListId value you obtained earlier in this activity, then in the API Explorer, within the Parameters section, paste the value in the bulkSendListId box.
3
Copy the envelopeId value you obtained earlier in this activity, then in the Body section, paste the value in the envelopeOrTemplateId box.
4
Click Get Response to send the request, then verify that the response includes a response code of 201 Created and the response body includes a value for the batchId property.
5
In the response body, select and copy the value of the batchId property, then paste the value into a separate file or note for use later in this activity.
Check Bulk Send Status
1
Click the CHECK STATUS button following this step to view the BulkSend: getBulkSendBatchStatus method in the Docusign Developer Center API Explorer.
Docusign API Explorer: BulkSend: getBulkSendBatchStatus
CHECK STATUS
2
Copy the bulkSendBatchId value you obtained earlier in this activity, then in the API Explorer, within the Parameters section, paste the value in the bulkSendBatchId box.
3
Click Get Response to send the request, then verify that the response includes a response code of 200 OK.
4
In the response body, check the values for the sent, queued, and failed properties.
5
If the queued value is not 0, wait a few seconds, submit the request again, and repeat if necessary until the response body shows no more envelopes are queued.
Lesson 5 - Activity: Prepare and Send a Bulk Envelope

### Implement Embedded Signing with the eSignature API 30 min

Implement Embedded Signing with the eSignature API
Introduction to Embedded Signing
IMPLEMENT EMBEDDED SIGNING
Create an Envelope with an Embedded Recipient
Generate an Embedded Signing URL
Embed the Recipient Signing URL
Embedded Signing Best Practices
Activity: Construct Embedded Signing Requests
Introduction to Embedded Signing
Deliver seamless signing experiences directly within your website or mobile application.
Docusign enables you to make agreements available to your recipients in two main ways:
Remote Signing: Recipients receive a link via email or another method you specify and click the link to open the agreement in a browser and review it.
Embedded Signing: You generate a signing URL and embed it in your application or website, so recipients can review and sign the agreement directly through it.
Embedded Signing Overview
There are two main methods for embedding signing into your application or website:
With focused view, you pass the signing URL into the Docusign JS library script and embed the script in the HTML of your application or website.
This method offers a minimal wrapper around the agreement document that shows only the agreement and a navigation button.
With classic view, you redirect the user to the signing URL or embed the signing URL in an iframe on your website.
Best Practice
Docusign recommends using focused view to implement embedded signing for most basic use cases. However, if you want to leverage features such as AI-Assisted Review, you must use classic view.
If your integration uses payment tabs, ID verification, or some types of standards-based signatures (SBS) pen providers, or if you want recipients to have access to AI-Assisted Review, you must build your embedded signing integration using classic view instead.
Note: If you prefer to use classic view but don't want signers to see the AI-Assisted Review feature, an account administrator can disable it in the account settings.
The Docusign JS library implements the loadDocuSign function to render a focused view agreement within an HTML element on your page.
You can import the library from https://js-d.docusign.com/bundle.js
for the developer environment or https://js.docusign.com/bundle.js
for the production environment.
Focused view provides the following benefits:
•
Fewer UI elements and easier to directly blend into your site.
•
Greater flexibility with colors and visual styles.
•
Automatic fallback to click-to-agree if no tabs are set for a recipient.
•
Easier event handling that you can use to trigger the next steps after the UI is loaded or after signing is complete.
Note: Optionally, you can embed an agreement in your HTML using Docusign JS without choosing to use focused view by setting the script’s displayFormat property to default. In this case, you would still gain the benefits of enabling your modals to open over the entire page and easier event handling, while using the classic agreement display format.
Enhancing Embedded Signing with Focused View
Select the button to the right to learn more about focused view benefits and implementation.
DOCUSIGN BLOG
See How
Embedded Signing with Focused View
Embedded Signing with Classic View
Implementing Embedded Signing Process Overview
Implementing embedded signing involves three main steps:
1
Create an envelope with an embedded recipient. This can be done by adding the clientUserId property to your Create Envelope request.
2
Generate the recipient signing URL.
3
Embed the signing process into your application or website.
If you are using focused view, you need to import the Docusign JS library and then pass the signing URL into the Docusign JS library script.
If you are using classic view, you can share the agreement with the recipient by redirecting them to the signing URL from your website or by rendering the signing URL in an iframe.
Lesson 2 - Create an Envelope with an Embedded Recipient

Implement Embedded Signing with the eSignature API
Introduction to Embedded Signing
IMPLEMENT EMBEDDED SIGNING
Create an Envelope with an Embedded Recipient
Generate an Embedded Signing URL
Embed the Recipient Signing URL
Embedded Signing Best Practices
Activity: Construct Embedded Signing Requests
Lesson 6 - Activity: Construct Embedded Signing Requests
Docusign University
Continue learning about the topics covered in this course. Search Docusign University to explore recommended content listed below. Click the link for your account type to register. (Customer
| Developer/Demo
| Employee
| Partner
)
Build Envelopes and Use Templates with the eSignature API
Additional Resources
Docusign Support
Docusign Community
Docusign on YouTube
Docusign Developer Center
Docusign IAM Platform
Create, commit to, and manage your agreements all in one collaborative platform.
What is the IAM Platform?
Docusign Certifications
Distinguish yourself as a Docusign expert by demonstrating your skills and experience with Docusign products and solutions.
Visit our certifications page or watch the video below to learn more about getting Docusign Certified. (Customers
| Developers
| Employees
| Partners
)
Lesson 8 - Course Complete

Implement Embedded Signing with the eSignature API
Introduction to Embedded Signing
IMPLEMENT EMBEDDED SIGNING
Create an Envelope with an Embedded Recipient
Generate an Embedded Signing URL
Embed the Recipient Signing URL
Embedded Signing Best Practices
Activity: Construct Embedded Signing Requests
Create an Envelope with an Embedded Recipient
Objective: After reviewing this topic, you will be able to create an envelope with an embedded recipient.
The first task for your code in response to a user request for an embedded signing experience is to create an envelope. Your request contains the envelope content and parameters. This task is identical whether you use focused or classic view.
The response from Docusign contains an envelopeId value, which is a unique GUID that your integration uses later in the embedded signing flow.
Endpoint
To create an envelope, you make a POST request to the Envelopes: create endpoint
at:
{baseUri}/{apiVersion}/accounts/{accountId}/envelopes
The accountId parameter is the Docusign account ID for the account making the API call, which varies between development and production accounts. To programmatically retrieve this value, you call the oauth/userinfo endpoint
after completing a supported OAuth flow.
Note: To learn about the OAuth flows supported by Docusign and how to integrate them into your app, enroll in the Implement Authentication with Docusign APIs self-paced learning plan in Docusign University (Customer
| Developer/Demo
| Employee
| Partner
).
Request
The Docusign eSignature REST API supports multiple ways to build an envelope.
•
Template: A request to create an envelope using a template requires you to identify the template and provide basic information for at least one template role.
•
Base64: Instead of using a template, you can build a request to create an envelope using one or more base64-encoded documents. To do so, you have to provide basic envelope parameters, including information on documents and recipients.
No matter which option you use, two parameters are always required for embedded signing: status and clientUserId. An additional parameter, identityVerification, is required for Part 11 support. This parameter can only be used with the classic view at this time.
Status
The status parameter indicates the requested status for the envelope. Embedded signing requires you to specify an envelope status of sent. This value enables signers to interact with the envelope immediately after it is created.
status: "sent"
clientUserId
The clientUserId parameter is a unique value specified by you. You can use this parameter to specify the recipient's user ID in your integration, or you can specify a minimal placeholder value like 1. Any non-null value for the clientUserId parameter indicates that your app is requesting an embedded signing experience for that recipient.
identityVerification
The identityVerification parameter specifies settings to verify the identity of the envelope signer for Part 11 requests. For 21 CFR Part 11 support, the identity verification method must be SMS.
Notes:
To create Part 11-compliant embedded signing requests, an account must be configured by Docusign as a Part 11 account. The account must also have SMS Authentication enabled.
The identityVerification parameter cannot be used with focused view at this time.
Select the following tabs to view JSON body examples for requests to create an envelope using a template and by providing base64 documents:
TEMPLATE
BASE64
Note: If you implement focused view with an envelope that contains no fields, the signer will be shown a clickwrap-style agreement experience with a button they can click to agree.
Try the Click To Agree tab in the Docusign Embedded Signing demo application
to test this signing experience.
Response
A successful response from the Envelopes: create endpoint includes an envelopeId parameter with a GUID as its value. You will use this value to create the next request in the embedded signing flow.
The following code shows an example response body for a request to create an envelope for embedded signing:
Docusign University
Continue learning about the topics covered in this course. Search Docusign University to explore recommended content listed below. Click the link for your account type to register. (Customer
| Developer/Demo
| Employee
| Partner
)
Build Envelopes and Use Templates with the eSignature API
Additional Resources
Docusign Support
Docusign Community
Docusign on YouTube
Docusign Developer Center
Docusign IAM Platform
Create, commit to, and manage your agreements all in one collaborative platform.
What is the IAM Platform?
Docusign Certifications
Distinguish yourself as a Docusign expert by demonstrating your skills and experience with Docusign products and solutions.
Visit our certifications page or watch the video below to learn more about getting Docusign Certified. (Customers
| Developers
| Employees
| Partners
)
Lesson 3 - Generate an Embedded Signing URL

Implement Embedded Signing with the eSignature API
Introduction to Embedded Signing
IMPLEMENT EMBEDDED SIGNING
Create an Envelope with an Embedded Recipient
Generate an Embedded Signing URL
Embed the Recipient Signing URL
Embedded Signing Best Practices
Activity: Construct Embedded Signing Requests
Generate an Embedded Signing URL
Objective: After reviewing this topic, you will be able to generate an embedded signing URL.
After generating an envelopeId, the next task to build an embedded signing flow is to obtain a URL for embedded signing. This URL is also referred to as a recipient view URL and is generated by Docusign for your user's signing experience.
Your recipient view URL request contains several parameters related to the user, envelope, and integration. If you are planning to use focused view, you will also need to include two additional parameters: frameAncestors and messageOrigins.
The response from Docusign contains a URL that your integration uses in the next step of the embedded signing flow.
Endpoint
To generate a recipient view URL, you make a POST request to the Envelope Views: createRecipient endpoint
at:
{baseUri}/{apiVersion}/accounts/{accountId}/envelopes/{envelopeId}/views/recipient
The endpoint URL incorporates the accountId for the authenticated user as well as the envelopeId for the envelope you created in the previous step.
Request
A request to create a recipient view URL for the standard and focused views includes values for four required parameters, as well as an optional parameter:
EMAIL, USERNAME, & CLIENTUSERID
RETURNURL
AUTHENTICATION METHOD
The required email, userName, and clientUserId parameters specify the recipient details. These values must match the email, name, and clientUserId parameter values you specified when you created the envelope in the previous step.
If you are planning to use focused view, you also must include the following two parameters:
FRAMEANCESTORS
MESSAGEORIGINS
The frameAncestors property is a string array that must include your site’s URL along with https://apps-d.docusign.com
if your app is in the demo environment or https://apps.docusign.com
if it is in production.
Your domain must have a valid SSL certificate (such as https://my.site.com) for embedding in production environments. You can use http://localhost for development and testing.
Response
A successful response from the Envelope Views: createRecipient endpoint
includes a url parameter with a url as its value. You will use this value to redirect the user in the next step of the embedded signing flow.
The following code shows an example response body for a request to create a recipient view for embedded signing:
Create an Envelope with an Embedded Recipient
Objective: After reviewing this topic, you will be able to create an envelope with an embedded recipient.
The first task for your code in response to a user request for an embedded signing experience is to create an envelope. Your request contains the envelope content and parameters. This task is identical whether you use focused or classic view.
The response from Docusign contains an envelopeId value, which is a unique GUID that your integration uses later in the embedded signing flow.
Endpoint
To create an envelope, you make a POST request to the Envelopes: create endpoint
at:
{baseUri}/{apiVersion}/accounts/{accountId}/envelopes
The accountId parameter is the Docusign account ID for the account making the API call, which varies between development and production accounts. To programmatically retrieve this value, you call the oauth/userinfo endpoint
after completing a supported OAuth flow.
Note: To learn about the OAuth flows supported by Docusign and how to integrate them into your app, enroll in the Implement Authentication with Docusign APIs self-paced learning plan in Docusign University (Customer
| Developer/Demo
| Employee
| Partner
).
Request
The Docusign eSignature REST API supports multiple ways to build an envelope.
•
Template: A request to create an envelope using a template requires you to identify the template and provide basic information for at least one template role.
•
Base64: Instead of using a template, you can build a request to create an envelope using one or more base64-encoded documents. To do so, you have to provide basic envelope parameters, including information on documents and recipients.
No matter which option you use, two parameters are always required for embedded signing: status and clientUserId. An additional parameter, identityVerification, is required for Part 11 support. This parameter can only be used with the classic view at this time.
Status
The status parameter indicates the requested status for the envelope. Embedded signing requires you to specify an envelope status of sent. This value enables signers to interact with the envelope immediately after it is created.
status: "sent"
clientUserId
The clientUserId parameter is a unique value specified by you. You can use this parameter to specify the recipient's user ID in your integration, or you can specify a minimal placeholder value like 1. Any non-null value for the clientUserId parameter indicates that your app is requesting an embedded signing experience for that recipient.
identityVerification
The identityVerification parameter specifies settings to verify the identity of the envelope signer for Part 11 requests. For 21 CFR Part 11 support, the identity verification method must be SMS.
Notes:
To create Part 11-compliant embedded signing requests, an account must be configured by Docusign as a Part 11 account. The account must also have SMS Authentication enabled.
The identityVerification parameter cannot be used with focused view at this time.
Select the following tabs to view JSON body examples for requests to create an envelope using a template and by providing base64 documents:
TEMPLATE
BASE64
Note: If you implement focused view with an envelope that contains no fields, the signer will be shown a clickwrap-style agreement experience with a button they can click to agree.
Try the Click To Agree tab in the Docusign Embedded Signing demo application
to test this signing experience.
Response
A successful response from the Envelopes: create endpoint includes an envelopeId parameter with a GUID as its value. You will use this value to create the next request in the embedded signing flow.
The following code shows an example response body for a request to create an envelope for embedded signing:
Lesson 4 - Embed the Recipient Signing URL

Implement Embedded Signing with the eSignature API
Introduction to Embedded Signing
IMPLEMENT EMBEDDED SIGNING
Create an Envelope with an Embedded Recipient
Generate an Embedded Signing URL
Embed the Recipient Signing URL
Embedded Signing Best Practices
Activity: Construct Embedded Signing Requests
Embed the Recipient Signing URL
Objective: After reviewing this topic, you will be able to embed the recipient signing URL into your integration.
Once you have generated the URL for the recipient view, the final step involves embedding the recipient signing URL into your application or website.
This step differs when you are using focused or classic view.
Embed the Signing URL with Focused View and Docusign JS
Once you have generated the signing URL, you can customize the focused view and embed it into your application or website.
First, load the Docusign JS library to turn on the focused view. The URL for the JS library is https://js-d.docusign.com/bundle.js
for the developer environment and https://js.docusign.com/bundle.js
for the production environment.
Next, create a signing configuration object to pass to the signing function. This object takes two parameters: style and displayFormat. Review each tab below for more information.
STYLE
DISPLAY FORMAT
You can use the style parameter to customize styles and blend the agreement with the rest of your application. For example:
The primaryButton property can be used to customize the button background and text colors.
The signingNavigation property can be used to specify custom colors for the primary button in the agreement.
The finishText property enables you to customize the text on the button when all the tabs have been completed and the agreement is ready to be signed.
The position property takes one of three values: bottom-left, bottom-right, and bottom-center, which changes the placement of the signing button.
See the Docusign JS for Embedded Signing Reference
on the Docusign Developer Center for the full list of supported properties.
Finally, create an HTML div element as the agreement container. The agreement is designed to occupy a height of 400px by default and the entire width of the div where it is embedded. We recommend overriding these defaults by defining the height and width of the div appropriately to ensure the agreement feels native to your website.
You can view code samples for this step on GitHub: Bash
, C#
, Java
, Node.js
, PHP
, Powershell
, Python
, or Ruby
Handle Agreement Events with Docusign JS
You can add event handlers with Docusign JS to set up the next steps and automate processes in your integration.
You specify event handlers using the signing.on function. Whenever you implement Docusign JS, these event handlers are available, even if your integration does not use focused view.
Two events are currently supported:
•
ready: Fires when the UI has been successfully loaded.
•
sessionEnd: Fires when signing is complete. One of the following reasons is passed to the event handler as the value of the sessionEndType property:
signing_complete
cancel
decline
exception
fax_pending
session_timeout
ttl_expired
viewing_complete
Embed the Signing URL with Classic View
When using classic view, you can either redirect the user's browser to the signing URL from your website or render the signing URL in an iframe
After being redirected, the user completes the signing experience on the docusign.com domain. When they are done signing, they are redirected to the URL you specified using the returnUrl parameter in your call to the EnvelopeViews: createRecipient endpoint in the previous step.
Best Practice
Your application can recover state information about the transaction by storing information in a cookie, or by including query parameters in the returnURL field, e.g., https://myapp.example.com/docusign_return?myState=12345
A query parameter in the form of event={event_type} is appended to the return URL and can be parsed by your app to determine what action the recipient took. Refer to the following linked resource for more details.
Signing Return Event Values
Select the Events button to view a list of possible values for the events parameter.
EVENTS
Generate an Embedded Signing URL
Objective: After reviewing this topic, you will be able to generate an embedded signing URL.
After generating an envelopeId, the next task to build an embedded signing flow is to obtain a URL for embedded signing. This URL is also referred to as a recipient view URL and is generated by Docusign for your user's signing experience.
Your recipient view URL request contains several parameters related to the user, envelope, and integration. If you are planning to use focused view, you will also need to include two additional parameters: frameAncestors and messageOrigins.
The response from Docusign contains a URL that your integration uses in the next step of the embedded signing flow.
Endpoint
To generate a recipient view URL, you make a POST request to the Envelope Views: createRecipient endpoint
at:
{baseUri}/{apiVersion}/accounts/{accountId}/envelopes/{envelopeId}/views/recipient
The endpoint URL incorporates the accountId for the authenticated user as well as the envelopeId for the envelope you created in the previous step.
Request
A request to create a recipient view URL for the standard and focused views includes values for four required parameters, as well as an optional parameter:
EMAIL, USERNAME, & CLIENTUSERID
RETURNURL
AUTHENTICATION METHOD
The required email, userName, and clientUserId parameters specify the recipient details. These values must match the email, name, and clientUserId parameter values you specified when you created the envelope in the previous step.
If you are planning to use focused view, you also must include the following two parameters:
FRAMEANCESTORS
MESSAGEORIGINS
The frameAncestors property is a string array that must include your site’s URL along with https://apps-d.docusign.com
if your app is in the demo environment or https://apps.docusign.com
if it is in production.
Your domain must have a valid SSL certificate (such as https://my.site.com) for embedding in production environments. You can use http://localhost for development and testing.
Response
A successful response from the Envelope Views: createRecipient endpoint
includes a url parameter with a url as its value. You will use this value to redirect the user in the next step of the embedded signing flow.
The following code shows an example response body for a request to create a recipient view for embedded signing:
Lesson 5 - Embedded Signing Best Practices

Implement Embedded Signing with the eSignature API
Introduction to Embedded Signing
IMPLEMENT EMBEDDED SIGNING
Create an Envelope with an Embedded Recipient
Generate an Embedded Signing URL
Embed the Recipient Signing URL
Embedded Signing Best Practices
Activity: Construct Embedded Signing Requests
Embedded Signing Best Practices
Objective: After reviewing this topic, you will be able to describe the best practices for implementing a Docusign embedded signing flow.
It is important to follow a few best practices when you implement embedded signing within your Docusign integration. Best practices vary depending on whether your integration is a browser-based web application or a native mobile application and whether you are using focused or classic view.
Browser-based Integrations
For focused view implementations, we recommend the following best practices:
•
Improve performance by loading the script asynchronously even before the signing URL is initialized in the loadDocuSign function.
•
Trigger the next steps using event handlers set in your focused view script.
•
Ensure that the focused view document fits correctly in any screen size by scaling the size of the div where it is mounted by a percentage rather than by an absolute number of pixels.
If you are using classic view, we recommend the following:
•
Let Docusign take full control of the browser window.
•
Properly size the frame when using framing.
•
If your integration will be used on mobile browsers, create a new browser tab instead of using an iframe.
Native Mobile App Integrations
The following best practices apply to native mobile app integrations:
•
Use a custom host for the returnUrl (such as https://yourappname/).
•
Return true when receiving URL changes that match your host to handle Docusign events.
•
For iOS, handle returnUrl with the webView:loadRequest method of WKWebView. To open the signing experience, an iOS app could use the following method to load the URL with WKWebView:
/*! @abstract Navigates to a requested URL.
@param request The request specifying the URL to which to navigate.
@result A new navigation for the given request. */
- (nullable WKNavigation *)loadRequest:(NSURLRequest *)request;
•
For Android, handle returnUrl with WebViewClient.shouldOverrideUrlLoading.
All Integrations
•
Your application should cache the clientUserId parameter for each recipient, which was sent when initiating the envelope.
•
Your application should make the API call to fetch the embedded signing URL only when the user is ready to sign the document, as the URL has a short-lived expiration period for security reasons.
•
The envelope ID for a specific customer should be stored in your own system so that it can be used for subsequent API calls. Every createEnvelope call will return an envelope ID.
•
•
Test the mobile experience for your integration on slower networks and ensure that your app keeps users engaged between the steps in the embedded signing process. Consider displaying a progress indicator before the document loads, and supplementing this with additional content that holds user interest on slower connections.
Embed the Recipient Signing URL
Objective: After reviewing this topic, you will be able to embed the recipient signing URL into your integration.
Once you have generated the URL for the recipient view, the final step involves embedding the recipient signing URL into your application or website.
This step differs when you are using focused or classic view.
Embed the Signing URL with Focused View and Docusign JS
Once you have generated the signing URL, you can customize the focused view and embed it into your application or website.
First, load the Docusign JS library to turn on the focused view. The URL for the JS library is https://js-d.docusign.com/bundle.js
for the developer environment and https://js.docusign.com/bundle.js
for the production environment.
Next, create a signing configuration object to pass to the signing function. This object takes two parameters: style and displayFormat. Review each tab below for more information.
STYLE
DISPLAY FORMAT
You can use the style parameter to customize styles and blend the agreement with the rest of your application. For example:
The primaryButton property can be used to customize the button background and text colors.
The signingNavigation property can be used to specify custom colors for the primary button in the agreement.
The finishText property enables you to customize the text on the button when all the tabs have been completed and the agreement is ready to be signed.
The position property takes one of three values: bottom-left, bottom-right, and bottom-center, which changes the placement of the signing button.
See the Docusign JS for Embedded Signing Reference
on the Docusign Developer Center for the full list of supported properties.
Finally, create an HTML div element as the agreement container. The agreement is designed to occupy a height of 400px by default and the entire width of the div where it is embedded. We recommend overriding these defaults by defining the height and width of the div appropriately to ensure the agreement feels native to your website.
You can view code samples for this step on GitHub: Bash
, C#
, Java
, Node.js
, PHP
, Powershell
, Python
, or Ruby
Handle Agreement Events with Docusign JS
You can add event handlers with Docusign JS to set up the next steps and automate processes in your integration.
You specify event handlers using the signing.on function. Whenever you implement Docusign JS, these event handlers are available, even if your integration does not use focused view.
Two events are currently supported:
•
ready: Fires when the UI has been successfully loaded.
•
sessionEnd: Fires when signing is complete. One of the following reasons is passed to the event handler as the value of the sessionEndType property:
signing_complete
cancel
decline
exception
fax_pending
session_timeout
ttl_expired
viewing_complete
Embed the Signing URL with Classic View
When using classic view, you can either redirect the user's browser to the signing URL from your website or render the signing URL in an iframe
After being redirected, the user completes the signing experience on the docusign.com domain. When they are done signing, they are redirected to the URL you specified using the returnUrl parameter in your call to the EnvelopeViews: createRecipient endpoint in the previous step.
Best Practice
Your application can recover state information about the transaction by storing information in a cookie, or by including query parameters in the returnURL field, e.g., https://myapp.example.com/docusign_return?myState=12345
A query parameter in the form of event={event_type} is appended to the return URL and can be parsed by your app to determine what action the recipient took. Refer to the following linked resource for more details.
Signing Return Event Values
Select the Events button to view a list of possible values for the events parameter.
EVENTS
Lesson 6 - Activity: Construct Embedded Signing Requests

Implement Embedded Signing with the eSignature API
Introduction to Embedded Signing
IMPLEMENT EMBEDDED SIGNING
Create an Envelope with an Embedded Recipient
Generate an Embedded Signing URL
Embed the Recipient Signing URL
Embedded Signing Best Practices
Activity: Construct Embedded Signing Requests
Complete the following steps to build an embedded signing flow with a series of API requests using Postman. The steps are sequenced and must be completed in order.
This activity can be completed in 10 minutes.
Setup
Download the following Embedded Signing Postman collection and environment:
Embedded Signing.postman_collection.json
4.3 KB
Embedded Signing.postman_environment.json
1 KB
Import the collection and environment you downloaded into a new workspace in Postman.
Specify the Embedded Signing environment as the active environment.
Download the following Docusign template file:
Mutual_NDA.zip
74.8 KB
In your browser, log in to your Docusign developer account, then click Templates, click Start, point to Envelope Templates, and click Upload Template.
Select the Mutual_NDA.zip file you downloaded above, then click Open to upload it.
From the Admin page, click Apps and Keys, then click Add App and Integration Key to create a new app.
Provide a name for your app.
Choose a classification for your app.
Note: To learn more about the different classifications, explore the Docusign Go-live
process on the Docusign Developer Center.
Click Add Secret Key to create a secret key, then copy the value.
In Postman, open the Embedded Signing environment, then paste your secret key as the value of the iSec variable.
In the Docusign settings for your new app, copy the value of your Integration Key, in Postman paste it as the value of the iKey variable, then save your changes to the Postman environment.
In the Docusign settings for your new app, click Add URI, enter https://oauth.pstmn.io/v1/callback, then click Save to save your changes to the app configuration.
In Postman, select the Embedded Signing collection folder, then on the Auth or Authorization tab, click Get New Access Token. Follow the prompts to log into your Docusign developer account and allow access to Postman to make requests on your behalf, then click Use Token to use the access token.
Note: When creating your own integration, you need to build your own authentication flow. To learn more about the available Docusign OAuth2 flows and how to implement them, complete the Implement Authentication with Docusign APIs learning path on Docusign University.
In the Postman collection, open the Get User Info request, then click Send.
Verify that you receive a response of 200 OK.
Create an Envelope
Next you need to create an envelope to be used for embedded signing.
In the Postman collection, open the Create Envelope request, then click the Body tab to view the request body.
Return to your Docusign Developer account in your browser, click Templates, click the NDA template you uploaded, click Template ID, then copy the value displayed.
Return to Postman, then on line 4, replace the placeholder value for the templateId property with the value you copied.
On line 8, replace the placeholder value for the email property with your email address, then on line 9, replace the placeholder value for the name property with your name.
Save your changes, then click Send. If your request was successful, the Response section contains an object with an envelopeId property.
Note: The Create Envelope Postman request automatically saves the returned envelopeId value as an environment variable for use in the next step.
Obtain a Signing URL
In the next step, you use the envelopeId value from the previous response to request a recipient signing URL.
Open the Create Embedded Signing Link request, then click the Body tab to view the request body.
On line 4, replace the placeholder value for the email property with the same email you entered in the previous set of steps, then on line 5, replace the placeholder value for the name property with the same name you entered previously.
If you wish, on line 2 replace the placeholder value for returnUrl with a URL of your choice. This is the URL that the recipient will be redirect to after signing is complete.
Note: If you change the returnUrl value, you must also add the new URL to the settings for your app in the Redirect URIs section.
Save your changes, then click Send. If your request was successful, the Response section contains an object with a url property. This URL expires in 5 minutes.
Navigate to the Signing URL with Focused View
In the final step, you open the generated signing URL to start the signing process.
Open the Focused View example front end
in a separate browser tab, then open the browser developer tools for that tab by pressing Ctrl + Shift + I (Windows) or command + option + I (Mac).
Click your browser's Reload button. The page reloads in debugging mode.
On the Console tab of your browser developer tools, set the value of the recipientViewUrl variable to the URL you generated in Postman:
recipientViewUrl = "https://demo.docusign.net/Signing/MTRedeem/v1/19d81c51-xxxx-xxxx-xxxx-c3435ab4e613?slt=eyJ0eX..."
Set the value of the clientId variable to the integration key for your app:
clientId = "cb556155-xxxx-xxxx-xxxx-6a4fd3a20e26"
Note: In a custom integration, your code would populate these variable values automatically.
Click the Resume script execution button to exit debugging mode. Your agreement opens in Focused View.
Sign the agreement, then click the Signed! button to end the focused view session.
In the browser developer tools Console tab, examine the sessionend message. This is generated by the Docusign JS script and specifies sessionEnd as the event type, signing_complete as the way the session ended, and the returnUrl value that would be opened after the signing session in a custom integration.
{
type: "sessionEnd",
sessionEndType: "signing_complete",
returnUrl: "http://127.0.0.1?event=signing_complete"
}
Navigate to the Signing URL with Classic View
In Postman, return to the Create Envelope request, then click Send to generate a new envelope.
Open the Create Embedded Signing Link request, then click Send to generate a new embedded signing link.
Copy the entire value of the url property (without the quotes) to the clipboard, open a new tab in your browser, then paste the URL in the address bar and open it. The embedded signing session for your envelope opens at docusign.com.
Note: In a custom integration, this redirect would be handled automatically by your code.
Sign and complete the agreement. Your browser is automatically redirects to http://127.0.0.1
or whichever redirect URL you specified when you created the embedded signing link. Note key-value pair event=signing_complete at the end of the URL.
Note: If your local system does not have a server running at http://127.0.0.1, the browser may display an error, which you can ignore. In a custom integration, the redirect URL value is generally either the page from which the embedded signing session was launched or a custom confirmation page.
Embedded Signing Best Practices
Objective: After reviewing this topic, you will be able to describe the best practices for implementing a Docusign embedded signing flow.
It is important to follow a few best practices when you implement embedded signing within your Docusign integration. Best practices vary depending on whether your integration is a browser-based web application or a native mobile application and whether you are using focused or classic view.
Browser-based Integrations
For focused view implementations, we recommend the following best practices:
•
Improve performance by loading the script asynchronously even before the signing URL is initialized in the loadDocuSign function.
•
Trigger the next steps using event handlers set in your focused view script.
•
Ensure that the focused view document fits correctly in any screen size by scaling the size of the div where it is mounted by a percentage rather than by an absolute number of pixels.
If you are using classic view, we recommend the following:
•
Let Docusign take full control of the browser window.
•
Properly size the frame when using framing.
•
If your integration will be used on mobile browsers, create a new browser tab instead of using an iframe.
Native Mobile App Integrations
The following best practices apply to native mobile app integrations:
•
Use a custom host for the returnUrl (such as https://yourappname/).
•
Return true when receiving URL changes that match your host to handle Docusign events.
•
For iOS, handle returnUrl with the webView:loadRequest method of WKWebView. To open the signing experience, an iOS app could use the following method to load the URL with WKWebView:
/*! @abstract Navigates to a requested URL.
@param request The request specifying the URL to which to navigate.
@result A new navigation for the given request. */
- (nullable WKNavigation *)loadRequest:(NSURLRequest *)request;
•
For Android, handle returnUrl with WebViewClient.shouldOverrideUrlLoading.
All Integrations
•
Your application should cache the clientUserId parameter for each recipient, which was sent when initiating the envelope.
•
Your application should make the API call to fetch the embedded signing URL only when the user is ready to sign the document, as the URL has a short-lived expiration period for security reasons.
•
The envelope ID for a specific customer should be stored in your own system so that it can be used for subsequent API calls. Every createEnvelope call will return an envelope ID.
•
•
Test the mobile experience for your integration on slower networks and ensure that your app keeps users engaged between the steps in the embedded signing process. Consider displaying a progress indicator before the document loads, and supplementing this with additional content that holds user interest on slower connections.

Implement Embedded Signing with the eSignature API
Introduction to Embedded Signing
IMPLEMENT EMBEDDED SIGNING
Create an Envelope with an Embedded Recipient
Generate an Embedded Signing URL
Embed the Recipient Signing URL
Embedded Signing Best Practices
Activity: Construct Embedded Signing Requests
Lesson 5 - Embedded Signing Best Practices
Activity: Construct Embedded Signing Requests
Complete the following steps to build an embedded signing flow with a series of API requests using Postman. The steps are sequenced and must be completed in order.
This activity can be completed in 10 minutes.
Setup
Download the following Embedded Signing Postman collection and environment:
Embedded Signing.postman_collection.json
4.3 KB
Embedded Signing.postman_environment.json
1 KB
Import the collection and environment you downloaded into a new workspace in Postman.
Specify the Embedded Signing environment as the active environment.
Download the following Docusign template file:
Mutual_NDA.zip
74.8 KB
In your browser, log in to your Docusign developer account, then click Templates, click Start, point to Envelope Templates, and click Upload Template.
Select the Mutual_NDA.zip file you downloaded above, then click Open to upload it.
From the Admin page, click Apps and Keys, then click Add App and Integration Key to create a new app.
Provide a name for your app.
Choose a classification for your app.
Note: To learn more about the different classifications, explore the Docusign Go-live
process on the Docusign Developer Center.
Click Add Secret Key to create a secret key, then copy the value.
In Postman, open the Embedded Signing environment, then paste your secret key as the value of the iSec variable.
In the Docusign settings for your new app, copy the value of your Integration Key, in Postman paste it as the value of the iKey variable, then save your changes to the Postman environment.
In the Docusign settings for your new app, click Add URI, enter https://oauth.pstmn.io/v1/callback, then click Save to save your changes to the app configuration.
In Postman, select the Embedded Signing collection folder, then on the Auth or Authorization tab, click Get New Access Token. Follow the prompts to log into your Docusign developer account and allow access to Postman to make requests on your behalf, then click Use Token to use the access token.
Note: When creating your own integration, you need to build your own authentication flow. To learn more about the available Docusign OAuth2 flows and how to implement them, complete the Implement Authentication with Docusign APIs learning path on Docusign University.
In the Postman collection, open the Get User Info request, then click Send.
Verify that you receive a response of 200 OK.
Create an Envelope
Next you need to create an envelope to be used for embedded signing.
In the Postman collection, open the Create Envelope request, then click the Body tab to view the request body.
Return to your Docusign Developer account in your browser, click Templates, click the NDA template you uploaded, click Template ID, then copy the value displayed.
Return to Postman, then on line 4, replace the placeholder value for the templateId property with the value you copied.
On line 8, replace the placeholder value for the email property with your email address, then on line 9, replace the placeholder value for the name property with your name.
Save your changes, then click Send. If your request was successful, the Response section contains an object with an envelopeId property.
Note: The Create Envelope Postman request automatically saves the returned envelopeId value as an environment variable for use in the next step.
Obtain a Signing URL
In the next step, you use the envelopeId value from the previous response to request a recipient signing URL.
Open the Create Embedded Signing Link request, then click the Body tab to view the request body.
On line 4, replace the placeholder value for the email property with the same email you entered in the previous set of steps, then on line 5, replace the placeholder value for the name property with the same name you entered previously.
If you wish, on line 2 replace the placeholder value for returnUrl with a URL of your choice. This is the URL that the recipient will be redirect to after signing is complete.
Note: If you change the returnUrl value, you must also add the new URL to the settings for your app in the Redirect URIs section.
Save your changes, then click Send. If your request was successful, the Response section contains an object with a url property. This URL expires in 5 minutes.
Navigate to the Signing URL with Focused View
In the final step, you open the generated signing URL to start the signing process.
Open the Focused View example front end
in a separate browser tab, then open the browser developer tools for that tab by pressing Ctrl + Shift + I (Windows) or command + option + I (Mac).
Click your browser's Reload button. The page reloads in debugging mode.
On the Console tab of your browser developer tools, set the value of the recipientViewUrl variable to the URL you generated in Postman:
recipientViewUrl = "https://demo.docusign.net/Signing/MTRedeem/v1/19d81c51-xxxx-xxxx-xxxx-c3435ab4e613?slt=eyJ0eX..."
Set the value of the clientId variable to the integration key for your app:
clientId = "cb556155-xxxx-xxxx-xxxx-6a4fd3a20e26"
Note: In a custom integration, your code would populate these variable values automatically.
Click the Resume script execution button to exit debugging mode. Your agreement opens in Focused View.
Sign the agreement, then click the Signed! button to end the focused view session.
In the browser developer tools Console tab, examine the sessionend message. This is generated by the Docusign JS script and specifies sessionEnd as the event type, signing_complete as the way the session ended, and the returnUrl value that would be opened after the signing session in a custom integration.
{
type: "sessionEnd",
sessionEndType: "signing_complete",
returnUrl: "http://127.0.0.1?event=signing_complete"
}
Navigate to the Signing URL with Classic View
In Postman, return to the Create Envelope request, then click Send to generate a new envelope.
Open the Create Embedded Signing Link request, then click Send to generate a new embedded signing link.
Copy the entire value of the url property (without the quotes) to the clipboard, open a new tab in your browser, then paste the URL in the address bar and open it. The embedded signing session for your envelope opens at docusign.com.
Note: In a custom integration, this redirect would be handled automatically by your code.
Sign and complete the agreement. Your browser is automatically redirects to http://127.0.0.1
or whichever redirect URL you specified when you created the embedded signing link. Note key-value pair event=signing_complete at the end of the URL.
Note: If your local system does not have a server running at http://127.0.0.1, the browser may display an error, which you can ignore. In a custom integration, the redirect URL value is generally either the page from which the embedded signing session was launched or a custom confirmation page.

Implement Embedded Signing with the eSignature API
Introduction to Embedded Signing
IMPLEMENT EMBEDDED SIGNING
Create an Envelope with an Embedded Recipient
Generate an Embedded Signing URL
Embed the Recipient Signing URL
Embedded Signing Best Practices
Activity: Construct Embedded Signing Requests
Embedded Signing Best Practices
Objective: After reviewing this topic, you will be able to describe the best practices for implementing a Docusign embedded signing flow.
It is important to follow a few best practices when you implement embedded signing within your Docusign integration. Best practices vary depending on whether your integration is a browser-based web application or a native mobile application and whether you are using focused or classic view.
Browser-based Integrations
For focused view implementations, we recommend the following best practices:
•
Improve performance by loading the script asynchronously even before the signing URL is initialized in the loadDocuSign function.
•
Trigger the next steps using event handlers set in your focused view script.
•
Ensure that the focused view document fits correctly in any screen size by scaling the size of the div where it is mounted by a percentage rather than by an absolute number of pixels.
If you are using classic view, we recommend the following:
•
Let Docusign take full control of the browser window.
•
Properly size the frame when using framing.
•
If your integration will be used on mobile browsers, create a new browser tab instead of using an iframe.
Native Mobile App Integrations
The following best practices apply to native mobile app integrations:
•
Use a custom host for the returnUrl (such as https://yourappname/).
•
Return true when receiving URL changes that match your host to handle Docusign events.
•
For iOS, handle returnUrl with the webView:loadRequest method of WKWebView. To open the signing experience, an iOS app could use the following method to load the URL with WKWebView:
/*! @abstract Navigates to a requested URL.
@param request The request specifying the URL to which to navigate.
@result A new navigation for the given request. */
- (nullable WKNavigation *)loadRequest:(NSURLRequest *)request;
•
For Android, handle returnUrl with WebViewClient.shouldOverrideUrlLoading.
All Integrations
•
Your application should cache the clientUserId parameter for each recipient, which was sent when initiating the envelope.
•
Your application should make the API call to fetch the embedded signing URL only when the user is ready to sign the document, as the URL has a short-lived expiration period for security reasons.
•
The envelope ID for a specific customer should be stored in your own system so that it can be used for subsequent API calls. Every createEnvelope call will return an envelope ID.
•
•
Test the mobile experience for your integration on slower networks and ensure that your app keeps users engaged between the steps in the embedded signing process. Consider displaying a progress indicator before the document loads, and supplementing this with additional content that holds user interest on slower connections.
Activity: Construct Embedded Signing Requests
Complete the following steps to build an embedded signing flow with a series of API requests using Postman. The steps are sequenced and must be completed in order.
This activity can be completed in 10 minutes.
Setup
Download the following Embedded Signing Postman collection and environment:
Embedded Signing.postman_collection.json
4.3 KB
Embedded Signing.postman_environment.json
1 KB
Import the collection and environment you downloaded into a new workspace in Postman.
Specify the Embedded Signing environment as the active environment.
Download the following Docusign template file:
Mutual_NDA.zip
74.8 KB
In your browser, log in to your Docusign developer account, then click Templates, click Start, point to Envelope Templates, and click Upload Template.
Select the Mutual_NDA.zip file you downloaded above, then click Open to upload it.
From the Admin page, click Apps and Keys, then click Add App and Integration Key to create a new app.
Provide a name for your app.
Choose a classification for your app.
Note: To learn more about the different classifications, explore the Docusign Go-live
process on the Docusign Developer Center.
Click Add Secret Key to create a secret key, then copy the value.
In Postman, open the Embedded Signing environment, then paste your secret key as the value of the iSec variable.
In the Docusign settings for your new app, copy the value of your Integration Key, in Postman paste it as the value of the iKey variable, then save your changes to the Postman environment.
In the Docusign settings for your new app, click Add URI, enter https://oauth.pstmn.io/v1/callback, then click Save to save your changes to the app configuration.
In Postman, select the Embedded Signing collection folder, then on the Auth or Authorization tab, click Get New Access Token. Follow the prompts to log into your Docusign developer account and allow access to Postman to make requests on your behalf, then click Use Token to use the access token.
Note: When creating your own integration, you need to build your own authentication flow. To learn more about the available Docusign OAuth2 flows and how to implement them, complete the Implement Authentication with Docusign APIs learning path on Docusign University.
In the Postman collection, open the Get User Info request, then click Send.
Verify that you receive a response of 200 OK.
Create an Envelope
Next you need to create an envelope to be used for embedded signing.
In the Postman collection, open the Create Envelope request, then click the Body tab to view the request body.
Return to your Docusign Developer account in your browser, click Templates, click the NDA template you uploaded, click Template ID, then copy the value displayed.
Return to Postman, then on line 4, replace the placeholder value for the templateId property with the value you copied.
On line 8, replace the placeholder value for the email property with your email address, then on line 9, replace the placeholder value for the name property with your name.
Save your changes, then click Send. If your request was successful, the Response section contains an object with an envelopeId property.
Note: The Create Envelope Postman request automatically saves the returned envelopeId value as an environment variable for use in the next step.
Obtain a Signing URL
In the next step, you use the envelopeId value from the previous response to request a recipient signing URL.
Open the Create Embedded Signing Link request, then click the Body tab to view the request body.
On line 4, replace the placeholder value for the email property with the same email you entered in the previous set of steps, then on line 5, replace the placeholder value for the name property with the same name you entered previously.
If you wish, on line 2 replace the placeholder value for returnUrl with a URL of your choice. This is the URL that the recipient will be redirect to after signing is complete.
Note: If you change the returnUrl value, you must also add the new URL to the settings for your app in the Redirect URIs section.
Save your changes, then click Send. If your request was successful, the Response section contains an object with a url property. This URL expires in 5 minutes.
Navigate to the Signing URL with Focused View
In the final step, you open the generated signing URL to start the signing process.
Open the Focused View example front end
in a separate browser tab, then open the browser developer tools for that tab by pressing Ctrl + Shift + I (Windows) or command + option + I (Mac).
Click your browser's Reload button. The page reloads in debugging mode.
On the Console tab of your browser developer tools, set the value of the recipientViewUrl variable to the URL you generated in Postman:
recipientViewUrl = "https://demo.docusign.net/Signing/MTRedeem/v1/19d81c51-xxxx-xxxx-xxxx-c3435ab4e613?slt=eyJ0eX..."
Set the value of the clientId variable to the integration key for your app:
clientId = "cb556155-xxxx-xxxx-xxxx-6a4fd3a20e26"
Note: In a custom integration, your code would populate these variable values automatically.
Click the Resume script execution button to exit debugging mode. Your agreement opens in Focused View.
Sign the agreement, then click the Signed! button to end the focused view session.
In the browser developer tools Console tab, examine the sessionend message. This is generated by the Docusign JS script and specifies sessionEnd as the event type, signing_complete as the way the session ended, and the returnUrl value that would be opened after the signing session in a custom integration.
{
type: "sessionEnd",
sessionEndType: "signing_complete",
returnUrl: "http://127.0.0.1?event=signing_complete"
}
Navigate to the Signing URL with Classic View
In Postman, return to the Create Envelope request, then click Send to generate a new envelope.
Open the Create Embedded Signing Link request, then click Send to generate a new embedded signing link.
Copy the entire value of the url property (without the quotes) to the clipboard, open a new tab in your browser, then paste the URL in the address bar and open it. The embedded signing session for your envelope opens at docusign.com.
Note: In a custom integration, this redirect would be handled automatically by your code.
Sign and complete the agreement. Your browser is automatically redirects to http://127.0.0.1
or whichever redirect URL you specified when you created the embedded signing link. Note key-value pair event=signing_complete at the end of the URL.
Note: If your local system does not have a server running at http://127.0.0.1, the browser may display an error, which you can ignore. In a custom integration, the redirect URL value is generally either the page from which the embedded signing session was launched or a custom confirmation page.
Lesson 6 - Activity: Construct Embedded Signing Requests

## Plan and Manage eSignature API Integrations

### Manage Envelopes with the eSignature API 15 min

Manage Envelopes with the eSignature API
Envelope Management Capabilities
Querying an Envelope
Modifying an Envelope Lifecycle
Modifying an Envelope Configuration or Contents
Activity
BUILDING YOUR INTEGRATION
Next Steps
Additional Resources
Envelope Management Capabilities
Stay on top of in-process envelopes and make modifications from within your custom app.
Docusign provides several tools for envelope management to query for information, modify an envelope lifecycle, and modify an envelope configuration or contents.
See How
Query an Envelope
When querying for information about a Docusign Envelope, you can:
•
Check on the status of your agreement, as well as other envelope information like details of recipient interactions.
•
Create custom logic to execute when the envelope has reached a certain lifecycle event, such as having been completed.
Modify an Envelope Lifecycle
When modifying an envelope lifecycle, you can:
•
Lock the envelope to temporarily prevent changes.
•
Void the envelope to cancel the agreement and end the envelope lifecycle.
Modify an Envelope Configuration or Contents
When modifying an envelope lifecycle, you can:
•
Change an envelope recipient list.
•
Change tabs associated with a specific recipient.
•
Replace a document within an envelope.
•
Add a new document to an envelope.
Lesson 2 - Querying an Envelope

Manage Envelopes with the eSignature API
Welcome to the Manage Envelopes with the eSignature API course. After reviewing this course, you will be able to:
Describe the methods available for managing in-process Docusign Envelopes.
Void or correct an envelope.
Envelope Management Capabilities
Querying an Envelope
Modifying an Envelope Lifecycle
Modifying an Envelope Configuration or Contents
Activity
BUILDING YOUR INTEGRATION
Next Steps
Additional Resources

Manage Envelopes with the eSignature API
Envelope Management Capabilities
Querying an Envelope
Modifying an Envelope Lifecycle
Modifying an Envelope Configuration or Contents
Activity
BUILDING YOUR INTEGRATION
Next Steps
Additional Resources
Lesson 5 - Activity
Next Steps
Objective: After reviewing this topic, you will be able to use Docusign tools to help you explore the eSignature API and build your integration.
Now that you understand how to manage in-process envelopes using the Docusign eSignature API, you are ready to write code to manage envelopes. Docusign offers several tools to get you started with basic app configuration and to help you explore calls to the Docusign eSignature API.
eSignature Quickstarts
A Docusign eSignature Quickstart is a personalized project in the programming language of your choice, configured with your developer account settings. You can use a wizard in the Docusign Developer Center to quickly set up and download a basic custom app that's ready to make API calls to the Docusign eSignature API.
Quickstart Wizard
Select the button to open the Quickstart wizard.
QUICKSTART
eSignature SDKs
Docusign provides SDKs to wrap our eSignature REST API with objects, properties, and methods in your favorite programming language. Supported languages include C#, Java, Node.js, PHP, Python, and Ruby. We also offer iOS and Android SDKs.
eSignature SDKs
Select the button to open the eSignature SDK directory.
SDKS
eSignature API Explorer
The Docusign API Explorer enables you to make requests to your developer account and learn how the Docusign eSignature API works. This browser-based tool is integrated with the API reference for each eSignature endpoint.
eSignature API Explorer
Select the button to open the eSignature API reference, then select an endpoint and click API Explorer.
API EXPLORER
Docusign REST API Postman Collections
Docusign offers Postman collections for the eSignature REST API as well as several other Docusign REST APIs. The eSignature REST collection includes requests organized by endpoint, as well as an Examples folder containing prebuilt example requests for several common tasks.
Docusign REST API Postman collections
Select the button to open the Docusign REST API Postman collections download list and instructions.
POSTMAN
Lesson 7 - Additional Resources

Manage Envelopes with the eSignature API
Envelope Management Capabilities
Querying an Envelope
Modifying an Envelope Lifecycle
Modifying an Envelope Configuration or Contents
Activity
BUILDING YOUR INTEGRATION
Next Steps
Additional Resources
Querying an Envelope
Objective: After reviewing this topic, you will be able to create an eSignature API request to modify the recipients, tabs, or documents of a Docusign envelope that has been sent.
Docusign provides a GET service for created envelopes. Any envelope with an ID can be queried to return information about the envelope. There are various reasons why you would want to query an envelope, and there are two primary practices when doing so. Review the sections below to learn about how to query information about a Docusign envelope using the eSignature API.
Manually Query an Envelope
You can query using a specific envelope ID to return information about an individual envelope .
You can also create a request based on envelope attributes that may return information about multiple envelopes. For instance, you may query for all envelopes sent within a given date range.
Docusign allows only 1 GET request per envelope every 15 minutes against the API, so it is not recommended you architect your application around polling for individual envelope statuses. Due to the API limits, you should restrict your use of this approach and use it with a specific intention.
You can read more about polling restrictions and approaches in the API usage guidelines
on the Docusign Developer Center.
Manage Status with a Webhook
Docusign has a service called Connect that listens for envelope status changes on your account. You can build a simple webhook listening application to act as a middleware listener. You then instruct Connect to point those events to your listener application. Setting up a webhook listener means your custom integration does not have to manually query envelopes to retrieve their status. When your listening application receives a message, the sole requirement is to send a response back to Docusign letting the API know that you received the message. Benefits to using a webhook instead of querying manually include the following:
•
The returned information does not count against your API request limits because Docusign sends it directly to you.
•
Messages are delivered to your listener only when an envelope event occurs, meaning that anytime your application might need to take action on an envelope, it will be automatically notified.
•
You avoid custom and cumbersome polling logic within your application that would have to manage the data returned and track when to query again.
Best Practice
Using a webhook to handle envelope lifecycle events is the recommended approach for reliable long-term envelope management.
Note:
Other querying mechanisms, such as querying the lock status of an envelope, are not covered in this topic. Please see the eSignature REST API reference for the Envelopes Category for more GET methods you can administer on an envelope.
API reference: Envelopes category
Click the Reference button to view the full eSignature REST API reference for the Envelopes category on the Docusign Developer Center.
REFERENCE
Next Steps
Objective: After reviewing this topic, you will be able to use Docusign tools to help you explore the eSignature API and build your integration.
Now that you understand how to manage in-process envelopes using the Docusign eSignature API, you are ready to write code to manage envelopes. Docusign offers several tools to get you started with basic app configuration and to help you explore calls to the Docusign eSignature API.
eSignature Quickstarts
A Docusign eSignature Quickstart is a personalized project in the programming language of your choice, configured with your developer account settings. You can use a wizard in the Docusign Developer Center to quickly set up and download a basic custom app that's ready to make API calls to the Docusign eSignature API.
Quickstart Wizard
Select the button to open the Quickstart wizard.
QUICKSTART
eSignature SDKs
Docusign provides SDKs to wrap our eSignature REST API with objects, properties, and methods in your favorite programming language. Supported languages include C#, Java, Node.js, PHP, Python, and Ruby. We also offer iOS and Android SDKs.
eSignature SDKs
Select the button to open the eSignature SDK directory.
SDKS
eSignature API Explorer
The Docusign API Explorer enables you to make requests to your developer account and learn how the Docusign eSignature API works. This browser-based tool is integrated with the API reference for each eSignature endpoint.
eSignature API Explorer
Select the button to open the eSignature API reference, then select an endpoint and click API Explorer.
API EXPLORER
Docusign REST API Postman Collections
Docusign offers Postman collections for the eSignature REST API as well as several other Docusign REST APIs. The eSignature REST collection includes requests organized by endpoint, as well as an Examples folder containing prebuilt example requests for several common tasks.
Docusign REST API Postman collections
Select the button to open the Docusign REST API Postman collections download list and instructions.
POSTMAN
Lesson 3 - Modifying an Envelope Lifecycle

Manage Envelopes with the eSignature API
Envelope Management Capabilities
Querying an Envelope
Modifying an Envelope Lifecycle
Modifying an Envelope Configuration or Contents
Activity
BUILDING YOUR INTEGRATION
Next Steps
Additional Resources
Modifying an Envelope Lifecycle
Objective: After reviewing this topic, you will be able to create an eSignature API request to manually modify the lifecycle of a Docusign envelope that has been sent.
The lifecycle of a Docusign envelope usually goes through the the following stages:
1
Created: The envelope is in a draft state and has not been sent out for signing.
2
Sent: An email notification with a link to the envelope has been sent to at least one recipient. The envelope remains in this state until all recipients have viewed it at a minimum.
3
Delivered: All recipients have viewed the document(s) in an envelope through the Docusign signing web site or your custom integration.
4
Signed: All recipients have taken action on the documents. This is a temporary state during processing, after which the envelope is automatically moved to Completed status.
5
Completed: The envelope has been completed by all the recipients, which completes its lifecycle.
Note: Docusign envelopes support additional status events. Review Envelope and recipient status codes
in the Docusign Developer Center for more detailed information about each status.
These lifecycle events occur naturally as recipients take action on the documents. Sometimes situations arise where agreements must be put on hold or the agreement must be canceled. In these cases, the status is modified manually. Therefore, the following additional lifecycle events are possible:
Correct: The envelope has been opened by the sender for correction. The signing process is stopped for envelopes with this status.
Voided: The envelope has been voided by the sender or has expired. The void reason indicates whether the envelope was manually voided or expired.
Either stage impacts all parties involved. When an envelope is in correct status, it is locked, which temporarily prevents recipients from signing. When an envelope has a status of voided, recipients are permanently prevented from signing.
The Docusign eSignature API provides methods for locking agreements and other methods to manually void agreements. Review the sections below to learn how to modify an envelope using correct and voided.
Note:
For an envelope in a terminal status (complete, declined, and voided) no further API modifications can be executed on the envelope.
Locking and Correcting Envelopes
If you need to put an envelope on hold, you can send a request to lock it and to change its status to correct. This does not void it. Instead, the envelope is placed on a temporary hold for a set duration, or until you manually unlock it. This is necessary when an envelope is being edited within your application and you need to prevent recipients from taking action on it while it is being edited.
To create a lock on an envelope, make a request to the EnvelopeLocks: create
endpoint and pass the accountId and envelopeId parameters within the header block. Within the API request body, you include the lockType, the name of the application that locked the envelope, and the lock duration in seconds.
The following code shows an example request body for a lock request:
Voiding Envelopes
Docusign provides a voiding method within the API to cancel agreements when necessary. This can be done at any time in the lifecycle of an envelope up until the agreement is completed, and it involves a manual status change.
To void an envelope, you call the Envelopes: update
endpoint. The request header must include the accountId and envelopeId. Within the request body, you include the status property with the value of voided and a voidedReason value describing the reason.
The following code shows an example request body for a void request:
Once this request is successful, the envelope will be voided and its lifecycle terminated for all recipients.
Note: When an envelope is locked or voided, it will impact all parties involved. Locks are temporary, voiding is permanent.
Querying an Envelope
Objective: After reviewing this topic, you will be able to create an eSignature API request to modify the recipients, tabs, or documents of a Docusign envelope that has been sent.
Docusign provides a GET service for created envelopes. Any envelope with an ID can be queried to return information about the envelope. There are various reasons why you would want to query an envelope, and there are two primary practices when doing so. Review the sections below to learn about how to query information about a Docusign envelope using the eSignature API.
Manually Query an Envelope
You can query using a specific envelope ID to return information about an individual envelope .
You can also create a request based on envelope attributes that may return information about multiple envelopes. For instance, you may query for all envelopes sent within a given date range.
Docusign allows only 1 GET request per envelope every 15 minutes against the API, so it is not recommended you architect your application around polling for individual envelope statuses. Due to the API limits, you should restrict your use of this approach and use it with a specific intention.
You can read more about polling restrictions and approaches in the API usage guidelines
on the Docusign Developer Center.
Manage Status with a Webhook
Docusign has a service called Connect that listens for envelope status changes on your account. You can build a simple webhook listening application to act as a middleware listener. You then instruct Connect to point those events to your listener application. Setting up a webhook listener means your custom integration does not have to manually query envelopes to retrieve their status. When your listening application receives a message, the sole requirement is to send a response back to Docusign letting the API know that you received the message. Benefits to using a webhook instead of querying manually include the following:
•
The returned information does not count against your API request limits because Docusign sends it directly to you.
•
Messages are delivered to your listener only when an envelope event occurs, meaning that anytime your application might need to take action on an envelope, it will be automatically notified.
•
You avoid custom and cumbersome polling logic within your application that would have to manage the data returned and track when to query again.
Best Practice
Using a webhook to handle envelope lifecycle events is the recommended approach for reliable long-term envelope management.
Note:
Other querying mechanisms, such as querying the lock status of an envelope, are not covered in this topic. Please see the eSignature REST API reference for the Envelopes Category for more GET methods you can administer on an envelope.
API reference: Envelopes category
Click the Reference button to view the full eSignature REST API reference for the Envelopes category on the Docusign Developer Center.
REFERENCE
Lesson 4 - Modifying an Envelope Configuration or Contents

Manage Envelopes with the eSignature API
Envelope Management Capabilities
Querying an Envelope
Modifying an Envelope Lifecycle
Modifying an Envelope Configuration or Contents
Activity
BUILDING YOUR INTEGRATION
Next Steps
Additional Resources
Modifying an Envelope Configuration or Contents
Objective: After reviewing this topic, you will be able to create an eSignature API request to modify the recipients, tabs, or documents of a Docusign envelope that has been sent.
Even after an agreement has been sent, you can use the Docusign API to make modifications. For example, agreements could require new recipients be added or new fields for signing placed on the document. Review the sections below to learn about the various ways you can modify the structure of an in-process envelope.
Changing Recipients Within Envelopes
Sometimes it is necessary to change recipients on an envelope, such as adding another signer. You can specify a change using the EnvelopeRecipients: update
method of the Docusign eSignature API. In the request header, you specify the accountId and envelopeId you are targeting. In the body, you include a new recipient object to replace the current one.
Changing Tabs Within Envelopes
You may find it necessary to update tabs for an envelope recipient, such as adding an additional initial tab along with a signature tab. You can use the Docusign eSignature API to modify tabs for specific recipients using the EnvelopeRecipientTabs: update
method. To accomplish this, follow these steps:
1
Make a GET request to retrieve the list of tabs for the recipient using the EnvelopeRecipientTabs: list
method.
2
Determine the tabs(s) and values that need to be updated and store the tabId for each tab.
3
Make a PUT request to update the tabs using the EnvelopeRecipientTabs: update
method.
As part of the endpoint URL, you specify which accountId, envelopeId, and recipientId you are targeting. In the update request body for the PUT request, include the entire tab object you plan to update, incorporating any changes you want to make.
Changing Documents Within Envelopes
In some cases, a document might need to be updated on an in-process envelope. In other cases, it might be necessary to add an additional document to the agreement. To accomplish this, you use the EnvelopeDocuments: update
method. You include the accountId, envelopeId, and documentId in the endpoint URI, and include the document data within the body. You can add new documents or update existing documents
You can also use the EnvelopeDocuments: delete
method to delete documents from an envelope.
Note:
Some in-process envelope changes cannot be executed based on the lifecycle status of the envelope and/or recipient. For instance, you cannot update a recipient that has already been completed, and tabs cannot be added to an envelope that is in a terminal status of completed, voided, or declined. For more information on specific rules, reference the API documentation for the operation required. For example, review the rules for envelope recipients
Modifying an Envelope Lifecycle
Objective: After reviewing this topic, you will be able to create an eSignature API request to manually modify the lifecycle of a Docusign envelope that has been sent.
The lifecycle of a Docusign envelope usually goes through the the following stages:
1
Created: The envelope is in a draft state and has not been sent out for signing.
2
Sent: An email notification with a link to the envelope has been sent to at least one recipient. The envelope remains in this state until all recipients have viewed it at a minimum.
3
Delivered: All recipients have viewed the document(s) in an envelope through the Docusign signing web site or your custom integration.
4
Signed: All recipients have taken action on the documents. This is a temporary state during processing, after which the envelope is automatically moved to Completed status.
5
Completed: The envelope has been completed by all the recipients, which completes its lifecycle.
Note: Docusign envelopes support additional status events. Review Envelope and recipient status codes
in the Docusign Developer Center for more detailed information about each status.
These lifecycle events occur naturally as recipients take action on the documents. Sometimes situations arise where agreements must be put on hold or the agreement must be canceled. In these cases, the status is modified manually. Therefore, the following additional lifecycle events are possible:
Correct: The envelope has been opened by the sender for correction. The signing process is stopped for envelopes with this status.
Voided: The envelope has been voided by the sender or has expired. The void reason indicates whether the envelope was manually voided or expired.
Either stage impacts all parties involved. When an envelope is in correct status, it is locked, which temporarily prevents recipients from signing. When an envelope has a status of voided, recipients are permanently prevented from signing.
The Docusign eSignature API provides methods for locking agreements and other methods to manually void agreements. Review the sections below to learn how to modify an envelope using correct and voided.
Note:
For an envelope in a terminal status (complete, declined, and voided) no further API modifications can be executed on the envelope.
Locking and Correcting Envelopes
If you need to put an envelope on hold, you can send a request to lock it and to change its status to correct. This does not void it. Instead, the envelope is placed on a temporary hold for a set duration, or until you manually unlock it. This is necessary when an envelope is being edited within your application and you need to prevent recipients from taking action on it while it is being edited.
To create a lock on an envelope, make a request to the EnvelopeLocks: create
endpoint and pass the accountId and envelopeId parameters within the header block. Within the API request body, you include the lockType, the name of the application that locked the envelope, and the lock duration in seconds.
The following code shows an example request body for a lock request:
Voiding Envelopes
Docusign provides a voiding method within the API to cancel agreements when necessary. This can be done at any time in the lifecycle of an envelope up until the agreement is completed, and it involves a manual status change.
To void an envelope, you call the Envelopes: update
endpoint. The request header must include the accountId and envelopeId. Within the request body, you include the status property with the value of voided and a voidedReason value describing the reason.
The following code shows an example request body for a void request:
Once this request is successful, the envelope will be voided and its lifecycle terminated for all recipients.
Note: When an envelope is locked or voided, it will impact all parties involved. Locks are temporary, voiding is permanent.
Lesson 5 - Activity

Manage Envelopes with the eSignature API
Envelope Management Capabilities
Querying an Envelope
Modifying an Envelope Lifecycle
Modifying an Envelope Configuration or Contents
Activity
BUILDING YOUR INTEGRATION
Next Steps
Additional Resources
Activity
Objective: After reviewing this topic, you will be able to add a recipient to an in-process envelope and void an in-process envelope.
Let's walk through the process of modifying an in-process envelope and then voiding it. Follow the steps below to complete the activity. The steps are sequenced and must be completed in order. This activity can be completed in 5 minutes.
Setup
Before beginning this activity, be sure you have created a Docusign developer account.
Send an Envelope
1
Click the CREATE ENVELOPE button following this step to view the Envelopes: create method in the Docusign Developer Center API Explorer, then log in if necessary.
Docusign API Explorer: Envelopes: create method
CREATE ENVELOPE
If you are using Postman instead of the API Explorer, open the eSignature API Postman collection, then open the Envelopes > Creates an Envelope (POST) request.
2
Copy the following code to the clipboard:
Note:
The preceding code box includes over 80 lines of code, including a lengthy base64 string. Be sure to select all the lines of code before copying.
3
In the API Explorer, at the start of the Body section, click JSON Editor, then paste the code you copied in place of the existing request body.
4
Click Get Response to send the request, then verify that you receive a response code of 201 Created, which indicates that the request was successful.
5
In the response body, select and copy the value of the envelopeId property, then paste the value into a separate file or note for use later in this activity.
Correct an Envelope
1
Click the UPDATE RECIPIENTS button following this step to view the EnvelopeRecipients: update method in the Docusign Developer Center API Explorer.
Docusign API Explorer: EnvelopeRecipients: update method
UPDATE RECIPIENTS
If you are using Postman instead of the API Explorer, open the eSignature API Postman collection, then open the Envelopes > Updates recipients in a draft envelope or corrects recipient information for an in process envelope (PUT) request.
2
Copy the envelopeId value from the envelope you sent in the previous set of steps, then within the Parameters section, paste the value you copied into the envelopeId box.
3
Copy the following code to the clipboard:
4
In the API Explorer, at the start of the Body section, click JSON Editor, then paste the code you copied in place of the existing request body.
5
Click Get Response to send the request, then verify that you receive a response code of 200 OK, which indicates that the request was successful.
6
Click the DOCUSIGN APP button following this step to open the Docusign eSignature app in your browser, then log in using your developer account.
Docusign eSignature App
DOCUSIGN APP
7
On the Manage tab, display your sent envelopes, then verify that the envelope with the subject Please Sign: Basic Nondisclosure Agreement has been updated to include the fourth recipient you just specified.
Void an Envelope
1
Click the UPDATE ENVELOPES button following this step to view the Envelopes: update method in the Docusign Developer Center API Explorer.
Docusign API Explorer: Envelopes: update method
UPDATE ENVELOPES
If you are using Postman instead of the API Explorer, open the eSignature API Postman collection, then open the Envelopes > Send Draft Envelope/Void Envelope/Move/Purge Envelope/Modify draft (PUT) request.
2
Copy the envelopeId value from the envelope you sent in the previous section, then within the Parameters section, paste the value you copied into the envelopeId box.
3
Copy the following code to the clipboard:
4
In the API Explorer, at the start of the Body section, click JSON Editor, then paste the code you copied in place of the existing request body.
5
Click Get Response to send the request, then verify that you receive a response code of 200 OK, which indicates that the request was successful.
6
Return to the Docusign eSignature app in your browser, refresh your list of sent envelopes, then verify that the envelope with the subject Please Sign: Basic Nondisclosure Agreement displays a status of Voided.
Modifying an Envelope Configuration or Contents
Objective: After reviewing this topic, you will be able to create an eSignature API request to modify the recipients, tabs, or documents of a Docusign envelope that has been sent.
Even after an agreement has been sent, you can use the Docusign API to make modifications. For example, agreements could require new recipients be added or new fields for signing placed on the document. Review the sections below to learn about the various ways you can modify the structure of an in-process envelope.
Changing Recipients Within Envelopes
Sometimes it is necessary to change recipients on an envelope, such as adding another signer. You can specify a change using the EnvelopeRecipients: update
method of the Docusign eSignature API. In the request header, you specify the accountId and envelopeId you are targeting. In the body, you include a new recipient object to replace the current one.
Changing Tabs Within Envelopes
You may find it necessary to update tabs for an envelope recipient, such as adding an additional initial tab along with a signature tab. You can use the Docusign eSignature API to modify tabs for specific recipients using the EnvelopeRecipientTabs: update
method. To accomplish this, follow these steps:
1
Make a GET request to retrieve the list of tabs for the recipient using the EnvelopeRecipientTabs: list
method.
2
Determine the tabs(s) and values that need to be updated and store the tabId for each tab.
3
Make a PUT request to update the tabs using the EnvelopeRecipientTabs: update
method.
As part of the endpoint URL, you specify which accountId, envelopeId, and recipientId you are targeting. In the update request body for the PUT request, include the entire tab object you plan to update, incorporating any changes you want to make.
Changing Documents Within Envelopes
In some cases, a document might need to be updated on an in-process envelope. In other cases, it might be necessary to add an additional document to the agreement. To accomplish this, you use the EnvelopeDocuments: update
method. You include the accountId, envelopeId, and documentId in the endpoint URI, and include the document data within the body. You can add new documents or update existing documents
You can also use the EnvelopeDocuments: delete
method to delete documents from an envelope.
Note:
Some in-process envelope changes cannot be executed based on the lifecycle status of the envelope and/or recipient. For instance, you cannot update a recipient that has already been completed, and tabs cannot be added to an envelope that is in a terminal status of completed, voided, or declined. For more information on specific rules, reference the API documentation for the operation required. For example, review the rules for envelope recipients
Lesson 6 - Next Steps

Manage Envelopes with the eSignature API
Envelope Management Capabilities
Querying an Envelope
Modifying an Envelope Lifecycle
Modifying an Envelope Configuration or Contents
Activity
BUILDING YOUR INTEGRATION
Next Steps
Additional Resources
Lesson 4 - Modifying an Envelope Configuration or Contents
Activity
Objective: After reviewing this topic, you will be able to add a recipient to an in-process envelope and void an in-process envelope.
Let's walk through the process of modifying an in-process envelope and then voiding it. Follow the steps below to complete the activity. The steps are sequenced and must be completed in order. This activity can be completed in 5 minutes.
Setup
Before beginning this activity, be sure you have created a Docusign developer account.
Send an Envelope
1
Click the CREATE ENVELOPE button following this step to view the Envelopes: create method in the Docusign Developer Center API Explorer, then log in if necessary.
Docusign API Explorer: Envelopes: create method
CREATE ENVELOPE
If you are using Postman instead of the API Explorer, open the eSignature API Postman collection, then open the Envelopes > Creates an Envelope (POST) request.
2
Copy the following code to the clipboard:
Note:
The preceding code box includes over 80 lines of code, including a lengthy base64 string. Be sure to select all the lines of code before copying.
3
In the API Explorer, at the start of the Body section, click JSON Editor, then paste the code you copied in place of the existing request body.
4
Click Get Response to send the request, then verify that you receive a response code of 201 Created, which indicates that the request was successful.
5
In the response body, select and copy the value of the envelopeId property, then paste the value into a separate file or note for use later in this activity.
Correct an Envelope
1
Click the UPDATE RECIPIENTS button following this step to view the EnvelopeRecipients: update method in the Docusign Developer Center API Explorer.
Docusign API Explorer: EnvelopeRecipients: update method
UPDATE RECIPIENTS
If you are using Postman instead of the API Explorer, open the eSignature API Postman collection, then open the Envelopes > Updates recipients in a draft envelope or corrects recipient information for an in process envelope (PUT) request.
2
Copy the envelopeId value from the envelope you sent in the previous set of steps, then within the Parameters section, paste the value you copied into the envelopeId box.
3
Copy the following code to the clipboard:
4
In the API Explorer, at the start of the Body section, click JSON Editor, then paste the code you copied in place of the existing request body.
5
Click Get Response to send the request, then verify that you receive a response code of 200 OK, which indicates that the request was successful.
6
Click the DOCUSIGN APP button following this step to open the Docusign eSignature app in your browser, then log in using your developer account.
Docusign eSignature App
DOCUSIGN APP
7
On the Manage tab, display your sent envelopes, then verify that the envelope with the subject Please Sign: Basic Nondisclosure Agreement has been updated to include the fourth recipient you just specified.
Void an Envelope
1
Click the UPDATE ENVELOPES button following this step to view the Envelopes: update method in the Docusign Developer Center API Explorer.
Docusign API Explorer: Envelopes: update method
UPDATE ENVELOPES
If you are using Postman instead of the API Explorer, open the eSignature API Postman collection, then open the Envelopes > Send Draft Envelope/Void Envelope/Move/Purge Envelope/Modify draft (PUT) request.
2
Copy the envelopeId value from the envelope you sent in the previous section, then within the Parameters section, paste the value you copied into the envelopeId box.
3
Copy the following code to the clipboard:
4
In the API Explorer, at the start of the Body section, click JSON Editor, then paste the code you copied in place of the existing request body.
5
Click Get Response to send the request, then verify that you receive a response code of 200 OK, which indicates that the request was successful.
6
Return to the Docusign eSignature app in your browser, refresh your list of sent envelopes, then verify that the envelope with the subject Please Sign: Basic Nondisclosure Agreement displays a status of Voided.
Lesson 6 - Next Steps

Manage Envelopes with the eSignature API
Envelope Management Capabilities
Querying an Envelope
Modifying an Envelope Lifecycle
Modifying an Envelope Configuration or Contents
Activity
BUILDING YOUR INTEGRATION
Next Steps
Additional Resources
Next Steps
Objective: After reviewing this topic, you will be able to use Docusign tools to help you explore the eSignature API and build your integration.
Now that you understand how to manage in-process envelopes using the Docusign eSignature API, you are ready to write code to manage envelopes. Docusign offers several tools to get you started with basic app configuration and to help you explore calls to the Docusign eSignature API.
eSignature Quickstarts
A Docusign eSignature Quickstart is a personalized project in the programming language of your choice, configured with your developer account settings. You can use a wizard in the Docusign Developer Center to quickly set up and download a basic custom app that's ready to make API calls to the Docusign eSignature API.
Quickstart Wizard
Select the button to open the Quickstart wizard.
QUICKSTART
eSignature SDKs
Docusign provides SDKs to wrap our eSignature REST API with objects, properties, and methods in your favorite programming language. Supported languages include C#, Java, Node.js, PHP, Python, and Ruby. We also offer iOS and Android SDKs.
eSignature SDKs
Select the button to open the eSignature SDK directory.
SDKS
eSignature API Explorer
The Docusign API Explorer enables you to make requests to your developer account and learn how the Docusign eSignature API works. This browser-based tool is integrated with the API reference for each eSignature endpoint.
eSignature API Explorer
Select the button to open the eSignature API reference, then select an endpoint and click API Explorer.
API EXPLORER
Docusign REST API Postman Collections
Docusign offers Postman collections for the eSignature REST API as well as several other Docusign REST APIs. The eSignature REST collection includes requests organized by endpoint, as well as an Examples folder containing prebuilt example requests for several common tasks.
Docusign REST API Postman collections
Select the button to open the Docusign REST API Postman collections download list and instructions.
POSTMAN
Activity
Objective: After reviewing this topic, you will be able to add a recipient to an in-process envelope and void an in-process envelope.
Let's walk through the process of modifying an in-process envelope and then voiding it. Follow the steps below to complete the activity. The steps are sequenced and must be completed in order. This activity can be completed in 5 minutes.
Setup
Before beginning this activity, be sure you have created a Docusign developer account.
Send an Envelope
1
Click the CREATE ENVELOPE button following this step to view the Envelopes: create method in the Docusign Developer Center API Explorer, then log in if necessary.
Docusign API Explorer: Envelopes: create method
CREATE ENVELOPE
If you are using Postman instead of the API Explorer, open the eSignature API Postman collection, then open the Envelopes > Creates an Envelope (POST) request.
2
Copy the following code to the clipboard:
Note:
The preceding code box includes over 80 lines of code, including a lengthy base64 string. Be sure to select all the lines of code before copying.
3
In the API Explorer, at the start of the Body section, click JSON Editor, then paste the code you copied in place of the existing request body.
4
Click Get Response to send the request, then verify that you receive a response code of 201 Created, which indicates that the request was successful.
5
In the response body, select and copy the value of the envelopeId property, then paste the value into a separate file or note for use later in this activity.
Correct an Envelope
1
Click the UPDATE RECIPIENTS button following this step to view the EnvelopeRecipients: update method in the Docusign Developer Center API Explorer.
Docusign API Explorer: EnvelopeRecipients: update method
UPDATE RECIPIENTS
If you are using Postman instead of the API Explorer, open the eSignature API Postman collection, then open the Envelopes > Updates recipients in a draft envelope or corrects recipient information for an in process envelope (PUT) request.
2
Copy the envelopeId value from the envelope you sent in the previous set of steps, then within the Parameters section, paste the value you copied into the envelopeId box.
3
Copy the following code to the clipboard:
4
In the API Explorer, at the start of the Body section, click JSON Editor, then paste the code you copied in place of the existing request body.
5
Click Get Response to send the request, then verify that you receive a response code of 200 OK, which indicates that the request was successful.
6
Click the DOCUSIGN APP button following this step to open the Docusign eSignature app in your browser, then log in using your developer account.
Docusign eSignature App
DOCUSIGN APP
7
On the Manage tab, display your sent envelopes, then verify that the envelope with the subject Please Sign: Basic Nondisclosure Agreement has been updated to include the fourth recipient you just specified.
Void an Envelope
1
Click the UPDATE ENVELOPES button following this step to view the Envelopes: update method in the Docusign Developer Center API Explorer.
Docusign API Explorer: Envelopes: update method
UPDATE ENVELOPES
If you are using Postman instead of the API Explorer, open the eSignature API Postman collection, then open the Envelopes > Send Draft Envelope/Void Envelope/Move/Purge Envelope/Modify draft (PUT) request.
2
Copy the envelopeId value from the envelope you sent in the previous section, then within the Parameters section, paste the value you copied into the envelopeId box.
3
Copy the following code to the clipboard:
4
In the API Explorer, at the start of the Body section, click JSON Editor, then paste the code you copied in place of the existing request body.
5
Click Get Response to send the request, then verify that you receive a response code of 200 OK, which indicates that the request was successful.
6
Return to the Docusign eSignature app in your browser, refresh your list of sent envelopes, then verify that the envelope with the subject Please Sign: Basic Nondisclosure Agreement displays a status of Voided.
Lesson 7 - Additional Resources

Manage Envelopes with the eSignature API
Envelope Management Capabilities
Querying an Envelope
Modifying an Envelope Lifecycle
Modifying an Envelope Configuration or Contents
Activity
BUILDING YOUR INTEGRATION
Next Steps
Additional Resources
Docusign University
Continue learning about the topics covered in this course. Search Docusign University to explore recommended content listed below. Click the link for your account type to register. (Customer
| Developer/Demo
| Employee
| Partner
)
Build Envelopes and Use Templates with the eSignature API
Configure Docusign Connect Webhooks with the eSignature API
Additional Resources
Docusign Support
Docusign Community
Docusign on YouTube
Docusign Developer Center
Docusign IAM
Create, commit to, and manage your agreements all in one collaborative platform.
What is Docusign IAM?
What can you do with Docusign IAM?
Visit the Docusign University IAM Learning Plans page to learn more about Docusign IAM. (Customers
| Developers
| Employees
| Partners
)
Docusign Certifications
Distinguish yourself as a Docusign expert by demonstrating your skills and experience with Docusign products and solutions.
Visit our certifications page or watch the video below to learn more about getting Docusign Certified. (Customers
| Developers
| Employees
| Partners
)
Next Steps
Objective: After reviewing this topic, you will be able to use Docusign tools to help you explore the eSignature API and build your integration.
Now that you understand how to manage in-process envelopes using the Docusign eSignature API, you are ready to write code to manage envelopes. Docusign offers several tools to get you started with basic app configuration and to help you explore calls to the Docusign eSignature API.
eSignature Quickstarts
A Docusign eSignature Quickstart is a personalized project in the programming language of your choice, configured with your developer account settings. You can use a wizard in the Docusign Developer Center to quickly set up and download a basic custom app that's ready to make API calls to the Docusign eSignature API.
Quickstart Wizard
Select the button to open the Quickstart wizard.
QUICKSTART
eSignature SDKs
Docusign provides SDKs to wrap our eSignature REST API with objects, properties, and methods in your favorite programming language. Supported languages include C#, Java, Node.js, PHP, Python, and Ruby. We also offer iOS and Android SDKs.
eSignature SDKs
Select the button to open the eSignature SDK directory.
SDKS
eSignature API Explorer
The Docusign API Explorer enables you to make requests to your developer account and learn how the Docusign eSignature API works. This browser-based tool is integrated with the API reference for each eSignature endpoint.
eSignature API Explorer
Select the button to open the eSignature API reference, then select an endpoint and click API Explorer.
API EXPLORER
Docusign REST API Postman Collections
Docusign offers Postman collections for the eSignature REST API as well as several other Docusign REST APIs. The eSignature REST collection includes requests organized by endpoint, as well as an Examples folder containing prebuilt example requests for several common tasks.
Docusign REST API Postman collections
Select the button to open the Docusign REST API Postman collections download list and instructions.
POSTMAN
Lesson 8 - Course Complete

Manage Envelopes with the eSignature API
Envelope Management Capabilities
Querying an Envelope
Modifying an Envelope Lifecycle
Modifying an Envelope Configuration or Contents
Activity
BUILDING YOUR INTEGRATION
Next Steps
Additional Resources
Lesson 6 - Next Steps
Additional Resources
Docusign University
Continue learning about the topics covered in this course. Search Docusign University to explore recommended content listed below. Click the link for your account type to register. (Customer
| Developer/Demo
| Employee
| Partner
)
Build Envelopes and Use Templates with the eSignature API
Configure Docusign Connect Webhooks with the eSignature API
Additional Resources
Docusign Support
Docusign Community
Docusign on YouTube
Watch a variety of Docusign University playlists that give you short, how-to tutorials when you need just a quick bit of learning, visit the Docusign YouTube Playlist
Docusign Developer Center
Docusign IAM
Create, commit to, and manage your agreements all in one collaborative platform.
What is Docusign IAM?
What can you do with Docusign IAM?
Visit the Docusign University IAM Learning Plans page to learn more about Docusign IAM. (Customers
| Developers
| Employees
| Partners
)
Docusign Certifications
Distinguish yourself as a Docusign expert by demonstrating your skills and experience with Docusign products and solutions.
Visit our certifications page or watch the video below to learn more about getting Docusign Certified. (Customers
| Developers
| Employees
| Partners
)
Lesson 8 - Course Complete

Manage Envelopes with the eSignature API
Envelope Management Capabilities
Querying an Envelope
Modifying an Envelope Lifecycle
Modifying an Envelope Configuration or Contents
Activity
BUILDING YOUR INTEGRATION
Next Steps
Additional Resources
Lesson 6 - Next Steps
Additional Resources
Docusign University
Continue learning about the topics covered in this course. Search Docusign University to explore recommended content listed below. Click the link for your account type to register. (Customer
| Developer/Demo
| Employee
| Partner
)
Build Envelopes and Use Templates with the eSignature API
Configure Docusign Connect Webhooks with the eSignature API
Additional Resources
Docusign Support
Docusign Community
Docusign on YouTube
Watch a variety of Docusign University playlists that give you short, how-to tutorials when you need just a quick bit of learning, visit the Docusign YouTube Playlist
Docusign Developer Center
To view API documentation, access developer resources, or obtain developer support, visit the Docusign Developer Center
Recommended resources:
Documentation: EnvelopeRecipients: update
Documentation: EnvelopeLocks: create
Overview: Envelopes
Docusign IAM
Create, commit to, and manage your agreements all in one collaborative platform.
What is Docusign IAM?
What can you do with Docusign IAM?
Visit the Docusign University IAM Learning Plans page to learn more about Docusign IAM. (Customers
| Developers
| Employees
| Partners
)
Docusign Certifications
Distinguish yourself as a Docusign expert by demonstrating your skills and experience with Docusign products and solutions.
Visit our certifications page or watch the video below to learn more about getting Docusign Certified. (Customers
| Developers
| Employees
| Partners
)
Lesson 8 - Course Complete

### Build a Custom eSignature Integration with CORS

Build a Custom eSignature Integration with CORS
Introduction to CORS for Docusign eSignature
CONFIGURE AND IMPLEMENT CORS
Configure CORS Options
Integrate eSignature Requests into a Single-Page Application
Activity: Make API Requests Using CORS
Introduction to CORS for Docusign eSignature
Securely integrate Docusign eSignature into custom applications without needing to configure a back-end server.
Cross-Origin Resource Sharing (CORS) is a modern web technology that enables developers to create applications that run in a web browser and communicate directly with services such as the Docusign eSignature REST API.
Enabling and configuring CORS for your eSignature application allows you to create an integration with front-end code only, for instance by building a single-page application (SPA). SPAs are often easier to create and faster to use because no back-end server is needed.
Note: Docusign also supports integration architectures using a back-end proxy as an alternative to CORS. Either pattern may be an appropriate choice, depending on the needs of your organization and your application.
CORS Overview
CORS
Select the OVERVIEW button to learn more about CORS on the Mozilla Developer Network.
OVERVIEW
Advantages
CORS brings advantages to building a custom eSignature API integration in a number of business situations, including the following:
Fast deployment: Quickly creating and deploying an internal line-of-business application.
Reducing data custody: For independent software vendors (ISVs), integrating Docusign into a product without passing customer data from Docusign APIs through the system.
Cost savings: Building an integration without incurring the cost of standing up and maintaining a back-end server.
Use Cases
Agreement Dashboard
eSignature Integration
Implementing CORS
Creating a single-page application that integrates with Docusign involves two parts.
Create and Configure Integration
Build eSignature API requests
Lesson 2 - Configure CORS Options

Build a Custom eSignature Integration with CORS
Welcome to the Build a Custom eSignature Integration with CORS course. After reviewing this course, you will be able to:
Describe what CORS is and the types of Docusign eSignature experiences it enables.
Configure the eSignature application settings required for a CORS integration.
Implement an eSignature API request using CORS.
Introduction to CORS for Docusign eSignature
CONFIGURE AND IMPLEMENT CORS
Configure CORS Options
Integrate eSignature Requests into a Single-Page Application
Activity: Make API Requests Using CORS

Build a Custom eSignature Integration with CORS
Introduction to CORS for Docusign eSignature
CONFIGURE AND IMPLEMENT CORS
Configure CORS Options
Integrate eSignature Requests into a Single-Page Application
Activity: Make API Requests Using CORS
Congratulations, you have completed this course!
Please provide feedback on this learning experience and content by completing the brief survey below.
Close the Course
EXIT

Build a Custom eSignature Integration with CORS
Introduction to CORS for Docusign eSignature
CONFIGURE AND IMPLEMENT CORS
Configure CORS Options
Integrate eSignature Requests into a Single-Page Application
Activity: Make API Requests Using CORS
Lesson 4 - Activity: Make API Requests Using CORS
Docusign University
Continue learning about the topics covered in this course. Search Docusign University to explore recommended content listed below. Click the link for your account type to register. (Customer
| Developer/Demo
| Employee
| Partner
)
Learning Plan: Implement Authentication with Docusign APIs
Learning Plan: Create and Configure Envelopes with the eSignature API
Additional Resources
Docusign Support
Docusign Community
Docusign on YouTube
Docusign Developer Center
Docusign IAM Platform
Create, commit to, and manage your agreements all in one collaborative platform.
What is the IAM Platform?
Docusign Certifications
Distinguish yourself as a Docusign expert by demonstrating your skills and experience with Docusign products and solutions.
Visit our certifications page or watch the video below to learn more about getting Docusign Certified. (Customers
| Developers
| Employees
| Partners
)
Lesson 6 - Course Complete

Build a Custom eSignature Integration with CORS
Introduction to CORS for Docusign eSignature
CONFIGURE AND IMPLEMENT CORS
Configure CORS Options
Integrate eSignature Requests into a Single-Page Application
Activity: Make API Requests Using CORS
Lesson 4 - Activity: Make API Requests Using CORS
Docusign University
Continue learning about the topics covered in this course. Search Docusign University to explore recommended content listed below. Click the link for your account type to register. (Customer
| Developer/Demo
| Employee
| Partner
)
Learning Plan: Implement Authentication with Docusign APIs
Learning Plan: Create and Configure Envelopes with the eSignature API
Additional Resources
Docusign Support
To learn more about a topic, obtain help with an issue, or search for support articles and tips, visit the Docusign Support Center
Docusign Community
Docusign on YouTube
Docusign Developer Center
Docusign IAM Platform
Create, commit to, and manage your agreements all in one collaborative platform.
What is the IAM Platform?
Docusign Certifications
Distinguish yourself as a Docusign expert by demonstrating your skills and experience with Docusign products and solutions.
Visit our certifications page or watch the video below to learn more about getting Docusign Certified. (Customers
| Developers
| Employees
| Partners
)
Lesson 6 - Course Complete

Build a Custom eSignature Integration with CORS
Introduction to CORS for Docusign eSignature
CONFIGURE AND IMPLEMENT CORS
Configure CORS Options
Integrate eSignature Requests into a Single-Page Application
Activity: Make API Requests Using CORS
Lesson 4 - Activity: Make API Requests Using CORS
Docusign University
Continue learning about the topics covered in this course. Search Docusign University to explore recommended content listed below. Click the link for your account type to register. (Customer
| Developer/Demo
| Employee
| Partner
)
Learning Plan: Implement Authentication with Docusign APIs
Learning Plan: Create and Configure Envelopes with the eSignature API
Additional Resources
Docusign Support
To learn more about a topic, obtain help with an issue, or search for support articles and tips, visit the Docusign Support Center
Docusign Community
To find answers to your questions, discuss best practices with other customers, or earn digital badges, visit the Docusign Community
Recommended topics:
Developers
eSignature API
Docusign on YouTube
Docusign Developer Center
Docusign IAM Platform
Create, commit to, and manage your agreements all in one collaborative platform.
What is the IAM Platform?
Docusign Certifications
Distinguish yourself as a Docusign expert by demonstrating your skills and experience with Docusign products and solutions.
Visit our certifications page or watch the video below to learn more about getting Docusign Certified. (Customers
| Developers
| Employees
| Partners
)
Lesson 6 - Course Complete

Build a Custom eSignature Integration with CORS
Introduction to CORS for Docusign eSignature
CONFIGURE AND IMPLEMENT CORS
Configure CORS Options
Integrate eSignature Requests into a Single-Page Application
Activity: Make API Requests Using CORS
Lesson 4 - Activity: Make API Requests Using CORS
Docusign University
Continue learning about the topics covered in this course. Search Docusign University to explore recommended content listed below. Click the link for your account type to register. (Customer
| Developer/Demo
| Employee
| Partner
)
Learning Plan: Implement Authentication with Docusign APIs
Learning Plan: Create and Configure Envelopes with the eSignature API
Additional Resources
Docusign Support
To learn more about a topic, obtain help with an issue, or search for support articles and tips, visit the Docusign Support Center
Docusign Community
To find answers to your questions, discuss best practices with other customers, or earn digital badges, visit the Docusign Community
Recommended topics:
Developers
eSignature API
Docusign on YouTube
Watch a variety of Docusign University playlists that give you short, how-to tutorials when you need just a quick bit of learning, visit the Docusign YouTube Playlist
Develop Custom Integrations with Docusign IAM
Docusign Developer Center
Docusign IAM Platform
Create, commit to, and manage your agreements all in one collaborative platform.
What is the IAM Platform?
Docusign Certifications
Distinguish yourself as a Docusign expert by demonstrating your skills and experience with Docusign products and solutions.
Visit our certifications page or watch the video below to learn more about getting Docusign Certified. (Customers
| Developers
| Employees
| Partners
)
Lesson 6 - Course Complete

## Docusign Workflow Builder API

### Build Agreement Workflows with Docusign 40 min

Build Agreement Workflows with Docusign
Introduction to Docusign Workflow Builder
Workflow Setup
Workflow Components
Create Workflows
Use and Manage Workflows
Introduction to Docusign Workflow Builder
Accelerate your agreement processes with customizable, code-free workflows that boost efficiency and reduce costs.
Whether it is documented or not, every organization has a process for creating and managing agreements. That process might be written down somewhere, modeled in a productivity tool, or stored in a spreadsheet tracker on someone’s desktop. It might simply be a routine followed from memory.
When teams manually transfer data between different documents and systems, it often leads to:
Delays, wasting time on manual data entry, and transfers;
Errors, increasing the risk of mistakes during data handling;
Lost revenue, slowing down the agreement process can impact sales and revenue.
A messy agreement process can also create a messy experience for customers, who do not want to get bogged down in redundant paperwork.
With Docusign Workflow Builder, you can build and deploy customizable agreement workflows that extend far beyond eSignature.
You can use the Workflow Builder to standardize the steps in your existing agreement workflows and make sure information flows easily and securely.
Common Use Cases
The Workflow Builder allows customers to build a variety of business processes, enabling them to digitalize their agreement journeys end-to-end. As you think about how workflows can streamline your current manual processes, consider the following use cases.
Lesson 2 - Workflow Setup

Build Agreement Workflows with Docusign
Welcome to the Build Agreement Workflows with Docusign course. After reviewing this course, you will be able to:
Complete setup actions
Create and manage workflows
Initiate and monitor workflow instances
Introduction to Docusign Workflow Builder
Workflow Setup
Workflow Components
Create Workflows
Use and Manage Workflows

Build Agreement Workflows with Docusign
Introduction to Docusign Workflow Builder
Workflow Setup
Workflow Components
Create Workflows
Use and Manage Workflows
Workflow Components
Objective: After reviewing this topic, you will be able to identify and choose between different workflow start methods and steps.
Start Methods
Start methods determine how your workflow will be initiated, and require certain configurations to run successfully. Workflows can be manually or automatically initiated.
Workflow Steps
Steps are the individual tasks executed in workflows. Your workflow can include:
Docusign Steps: Steps for Docusign features like ID Verification, Web Forms, and eSignature.
Utility Steps: Notification actions, such as sending an email, and workflow control actions, such as adding branch rules.
Apps Steps: Third-party extensions like Google Drive and Salesforce to automate your agreement process end-to-end.
Note: If Agreement Desk is enabled in your account, specific Agreement Desk steps will be available in Workflow Builder. To learn more, access the Configure and Manage Requests with Docusign Agreement Desk course in the Docusign University learning portal.
Docusign Steps
Collect Data with Web Forms Step
Prepare Document Template Step
Prepare eSignature Template Step
Send Documents for Signature
Use eSignature API Step
Identity Verification Steps
Note: Use the Prepare eSignature Template Step if you have a single template that can be used for all workflow instances. In this case, the document being signed is always exactly the same.
If you need to generate different documents based on workflow variables, use the Prepare Document Template. Use conditional show/hide logic defined on the template to generate different document content based on field values, meeting a wide variety of complex business requirements.
Both steps should be followed by the Send for Signature Step.
Utility Steps
Branching Steps
Set Up Invite Step
Send an Email Step
Show a Confirmation Screen Step
Apps Steps
Docusign Workflow Builder is designed to be extensible to third-party products through extension apps that an admin has authorized for your account, such as archiving a file to a cloud storage site or verifying bank account data. These applications integrate third-party functionality directly into the Workflow Builder platform, allowing you to include workflow steps that trigger actions in external systems.
Administrators can install these extension apps from Docusign App Center
Docusign Workflow Builder supports integrations with various categories of third-party applications:
Read Steps: Import data from external systems into your workflow. Extension apps available include Salesforce, HubSpot, and Dynamics 365.
Store Files Steps: Automate the storage of completed agreements and ID Evidence data. Extension apps available include Google Drive, Box, Dropbox, Salesforce, OneDrive, and SharePoint.
Writeback Steps: Automate information update to external systems. Extension apps available include Salesforce, HubSpot, Stripe, ServiceNow, and Dynamics 365.
| Developer/Demo
| Employee
| Partner
)
Configure Docusign Apps
For a full list of available apps and configuration information, visit Docusign Support.
Docusign University
Continue learning about the topics covered in this course. Search Docusign University to explore recommended content listed below. Click the link for your account type to register. (Customer
| Developer/Demo
| Employee
| Partner
)
Get Started with Docusign Workflow Builder
Build Custom Agreement Workflows with Docusign
Video Playlist: Docusign Workflow Builder
Configure and Manage Requests with Docusign Agreement Desk
Build Extension Apps for the Docusign App Center
Video Playlist: Docusign App Center: Discover Extension Apps
Additional Resources
Docusign Support
Docusign Community
Docusign on YouTube
Docusign Developer Center
Docusign IAM Platform
Create, commit to, and manage your agreements all in one collaborative platform.
What is the IAM Platform?
Docusign Certifications
Distinguish yourself as a Docusign expert by demonstrating your skills and experience with Docusign products and solutions.
Visit our certifications page or watch the video below to learn more about getting Docusign Certified. (Customers
| Developers
| Employees
| Partners
)
Lesson 4 - Create Workflows

Build Agreement Workflows with Docusign
Introduction to Docusign Workflow Builder
Workflow Setup
Workflow Components
Create Workflows
Use and Manage Workflows
Create Workflows
Objective: After reviewing this topic, you will be able to create and publish a workflow.
You can build workflows_from a new canvas, from a workflow template, from an eSignature template, from a Web Form, or by importing a workflow.
Onboarding Use Case
Let's look at an example of an end-to-end workflow that focuses on streamlining the new hire onboarding process at a global company.
Before implementing Docusign Workflow Builder, our Human Resources teams navigated a manual, slow, and often overwhelming new hire onboarding experience. HR representatives were responsible for manually forwarding various documents for signature based on new hire responses, such as location and type of contract, and then tracking their completion.
With Workflow Builder, we've successfully automated the onboarding experience. This has significantly saved HR representatives' time, enabled automatic status updates to all relevant parties, and ensured all documents are organized and securely stored.
Paul, Human Resources Manager
For this onboarding process, an offer letter must be generated, signed, and stored. Once that is done, workers should have their identity verified before signing their specific employment contracts, which will be based on their location (US or other) and job designation (remote or in-office). At any time, if a step is not completed by the new hire, the HR representative should be notified.
This example will focus on fully building the US new hire workflow. Workers based outside the US will be directed to their local Human Resources.
The solution for this use case can be automated through Workflow Builder in three stages:
1
Generate the Offer Letter
Collect New Hire information, use it to generate the offer letter, have it routed for signatures, and store it in Google Drive.
2
Complete Identity Verification
Verify the identity of workers located in the US and notify local Human Resources partners of international workers.
3
Sign Employment Contract
Based on the job designation (remote or in-office), contracts should be routed for signature.
Note: A workflow setup is required, which includes preparing any Web Forms or eSiganature Templates. For this use case, the New Hire Information Web Form should be created, as well as the Templates for the Offer Letter and Employment Contract.
Once you have identified all the components your workflow will need, you are ready to begin. From the Agreements tab, click Workflows in the menu, then click Create Workflow.
Generate the Offer Letter
In the first stage of the workflow, you will collect the relevant participant data and generate the offer letter for signature.
Use Case Needs
Workflow Implementation
Workflow Start
Include Participants: New Hire, HR Representative, Hiring Manager
Choose starting method:
Manually in Docusign
The HR Representative
receives and completes the New Hire Information form.
Collect Data with Web Forms Step: New Hire Information
Data from the New Hire Information form is automatically added to the Offer Letter template, which is routed to the New Hire and the Hiring Manager for signature.
Prepare eSignature Template Step: Create Offer Letter
Send Documents for Signature Step: Send Offer Letter
If the document is signed, it should be properly stored.
If the document is not signed, the HR Representative should be notified.
Branching Rule Step:
Envelope Status = completed
True: Offer Letter is stored in Google Drive
False: HR Rep is notified
Note: Participants were included at the beginning of the workflow creation process as a best practice, but you can add participants at any point during workflow creation. Anyone who will need to take action in this workflow is a participant, and will need a defined role, based on the actions they need to take and the documents they need to use.
Complete Identity Verification
For this example, we are building the US new hire workflow. Before proceeding to the Identity Verification of the workers located in the US, we first need to differentiate US workers from workers abroad. To do that, we can use a Multi Branch Rule step.
Use Case Needs
Workflow Implementation
Different work contracts for different workers:
US Worker or International Worker
Multi Branching Rule Step:
Job Location
US, Other, No Conditions Met
If the New Hire is located in the US, their identity should be verified.
Set Up Invite Step: Invite New Hire to verify their identity
Verify Someone's Identity Step
If the New Hire is located abroad, the local HR partner should be notified.
Send an Email Step: Local HR partner is notified
If the worker's location can not be identified, the HR Representative should be notified.
Send an Email Step: HR Rep is notified the workflow failed
Best Practice
Save your workflow draft as you add steps to it. Your draft is not automatically saved.
Sign Employment Contract
At the last stage, new hires should be able to sign their work contracts based on their job designation. A Multi Branch Rule step will be used, so different paths can be created.
Use Case Needs
Workflow Implementation
If the identity verification is successful, the contracts should be routed by Job Designation.
If the identity verification fails, the HR Representative should be notified.
Branching Rule Step: Validated = True
True: Multi Branch Rule Step - Job Designation
Remote, In Office, No Conditions Met
False: Send an Email Step - HR Rep is notified IDV failed
If the New Hire is a remote worker, they should receive the contract for remote workers.
Prepare eSignature Template Step: Remote Packet
Send Documents for Signature Step: Remote Packet
If the New Hire will work in office, they should receive the contract for in-office workers.
Prepare eSignature Template Step: In Office Packet
Send Documents for Signature Step: In Office Packet
If the worker's designation can not be identified, the HR Representative should be notified.
Send an Email Step: HR Rep is notified that the workflow failed
Review and Publish
When a workflow has been completed and is ready for deployment, the final step is to Review and Publish it, by clicking Review & Publish.
The system will check for errors, which you must resolve before publishing. You can define the naming convention of your workflow instances to ensure it meets all your requirements.
Once a workflow is published, it becomes available to anyone on your account with the proper workflow permissions.
Workflow Components
Objective: After reviewing this topic, you will be able to identify and choose between different workflow start methods and steps.
Start Methods
Start methods determine how your workflow will be initiated, and require certain configurations to run successfully. Workflows can be manually or automatically initiated.
Workflow Steps
Steps are the individual tasks executed in workflows. Your workflow can include:
Docusign Steps: Steps for Docusign features like ID Verification, Web Forms, and eSignature.
Utility Steps: Notification actions, such as sending an email, and workflow control actions, such as adding branch rules.
Apps Steps: Third-party extensions like Google Drive and Salesforce to automate your agreement process end-to-end.
Note: If Agreement Desk is enabled in your account, specific Agreement Desk steps will be available in Workflow Builder. To learn more, access the Configure and Manage Requests with Docusign Agreement Desk course in the Docusign University learning portal.
Docusign Steps
Collect Data with Web Forms Step
Prepare Document Template Step
Prepare eSignature Template Step
Send Documents for Signature
Use eSignature API Step
Identity Verification Steps
Note: Use the Prepare eSignature Template Step if you have a single template that can be used for all workflow instances. In this case, the document being signed is always exactly the same.
If you need to generate different documents based on workflow variables, use the Prepare Document Template. Use conditional show/hide logic defined on the template to generate different document content based on field values, meeting a wide variety of complex business requirements.
Both steps should be followed by the Send for Signature Step.
Utility Steps
Branching Steps
Set Up Invite Step
Send an Email Step
Show a Confirmation Screen Step
Apps Steps
Docusign Workflow Builder is designed to be extensible to third-party products through extension apps that an admin has authorized for your account, such as archiving a file to a cloud storage site or verifying bank account data. These applications integrate third-party functionality directly into the Workflow Builder platform, allowing you to include workflow steps that trigger actions in external systems.
Administrators can install these extension apps from Docusign App Center
Docusign Workflow Builder supports integrations with various categories of third-party applications:
Read Steps: Import data from external systems into your workflow. Extension apps available include Salesforce, HubSpot, and Dynamics 365.
Store Files Steps: Automate the storage of completed agreements and ID Evidence data. Extension apps available include Google Drive, Box, Dropbox, Salesforce, OneDrive, and SharePoint.
Writeback Steps: Automate information update to external systems. Extension apps available include Salesforce, HubSpot, Stripe, ServiceNow, and Dynamics 365.
| Developer/Demo
| Employee
| Partner
)
Configure Docusign Apps
For a full list of available apps and configuration information, visit Docusign Support.
Lesson 5 - Use and Manage Workflows

Build Agreement Workflows with Docusign
Introduction to Docusign Workflow Builder
Workflow Setup
Workflow Components
Create Workflows
Use and Manage Workflows
Objective: After reviewing this topic, you will be able to initiate workflows and manage running instances.
All users with Workflow Prepare permissions can initiate workflows published to your account.
Users with Workflow Create permissions can edit and republish any workflows that they have created.
Initiate a Workflow
Depending on which start method you used when creating your workflow, you will initiate the workflow in different ways.
MANUALLY TRIGGERED
AUTOMATICALLY TRIGGERED
Workflows can start from an action that is performed manually.
From a link: Someone opens a URL, and this starts the workflow. Choose this method for workflows that will be initiated by a participant, such as embedding a link on a website or in an automatic email response.
Manually in Docusign: Someone starts the workflow in the Workflow Builder. Choose this method for workflows that will be initiated by someone in your organization, such as a rental application process.
Learn More
Visit Docusign Support to learn more about using these start methods.
Run Workflow
For workflows starting manually in Docusign, click the three dots next to the desired workflow and choose Run Workflow. Anyone in your organization with Workflows: Prepare permissions will see all published workflows and can start workflows with this method. This method is similar to using a template where you populate recipient information and trigger the process, such as sending a rental application to an approved tenant.
Use Link
For workflows starting from a link, click the link icon next to the workflow to copy the URL and embed it in a website or automated email reply. This method is recommended for self-service forms such account change requests or client intake forms.
Manage Existing Workflows
Process Builders can manage any workflows they have created. The managing actions include:
Edit
Edit any of your saved drafts, published, paused, or unpublished workflows. You can add steps, modify steps, adjust participants, or change the workflow name.
If you Edit the participants or workflow steps, current active instances will not be modified, but new instances will reflect your changes.
Pause Instances
Any active instances will continue to run but no new instances can be initiated. Note:
A workflow that has been paused counts toward your workflow quota.
Changes made to a paused workflow can not be published.
A paused workflow can be resumed at any time.
Unpublish
If you are not using a workflow and you want to free up your workflow capacity, you can unpublish it, and it will remain in your account. Note:
You can only unpublish a workflow that has been paused.
No instances should be running to unpublish a workflow.
Unpublished workflows do not count toward your workflow quota.
An unpublished workflow can be published at any time.
Delete
You can permanently delete any workflow that has been unpublished. Note that you cannot recover a deleted workflow.
Export and Import
Exporting and importing a workflow allows you to move workflows or copies between accounts and environments. Note:
Step details and configurations are preserved in the export and import processes.
Any resources referenced in the steps are added to the account when the workflow is imported. This includes Web Forms and eSignature Templates.
All field mappings configured in the workflow steps are preserved.
Best Practices
Create and test new workflows in your demo account, export them, and then import the workflows into the production environment.
Export a workflow to make a new version or share with another Docusign user to preserve the current version of your workflow.
View Activity Log
Activity Logs provide full visibility into all actions taken across your workflows.
Manage Running Instances
Users with both Create and Use permissions can take the following actions:
View running instances - From the Workflows tab, click the Actions menu and select View Details to see all running, completed, and canceled instances of the workflow.
View instance details - From the Workflows page, click View Instances, then click View details next to the desired instance. This shows which steps have been completed, which step is active, and which steps are incomplete. Click View Details on a step to view additional details, such as participant name, completed date and time, and step ID.
Cancel an instance - From the instance view, click the Actions menu next to an instance and select Cancel. Data collected up to this point will be stored, but no further workflow steps will be triggered.
Create Workflows
Objective: After reviewing this topic, you will be able to create and publish a workflow.
You can build workflows_from a new canvas, from a workflow template, from an eSignature template, from a Web Form, or by importing a workflow.
Onboarding Use Case
Let's look at an example of an end-to-end workflow that focuses on streamlining the new hire onboarding process at a global company.
Before implementing Docusign Workflow Builder, our Human Resources teams navigated a manual, slow, and often overwhelming new hire onboarding experience. HR representatives were responsible for manually forwarding various documents for signature based on new hire responses, such as location and type of contract, and then tracking their completion.
With Workflow Builder, we've successfully automated the onboarding experience. This has significantly saved HR representatives' time, enabled automatic status updates to all relevant parties, and ensured all documents are organized and securely stored.
Paul, Human Resources Manager
For this onboarding process, an offer letter must be generated, signed, and stored. Once that is done, workers should have their identity verified before signing their specific employment contracts, which will be based on their location (US or other) and job designation (remote or in-office). At any time, if a step is not completed by the new hire, the HR representative should be notified.
This example will focus on fully building the US new hire workflow. Workers based outside the US will be directed to their local Human Resources.
The solution for this use case can be automated through Workflow Builder in three stages:
1
Generate the Offer Letter
Collect New Hire information, use it to generate the offer letter, have it routed for signatures, and store it in Google Drive.
2
Complete Identity Verification
Verify the identity of workers located in the US and notify local Human Resources partners of international workers.
3
Sign Employment Contract
Based on the job designation (remote or in-office), contracts should be routed for signature.
Note: A workflow setup is required, which includes preparing any Web Forms or eSiganature Templates. For this use case, the New Hire Information Web Form should be created, as well as the Templates for the Offer Letter and Employment Contract.
Once you have identified all the components your workflow will need, you are ready to begin. From the Agreements tab, click Workflows in the menu, then click Create Workflow.
Generate the Offer Letter
In the first stage of the workflow, you will collect the relevant participant data and generate the offer letter for signature.
Use Case Needs
Workflow Implementation
Workflow Start
Include Participants: New Hire, HR Representative, Hiring Manager
Choose starting method:
Manually in Docusign
The HR Representative
receives and completes the New Hire Information form.
Collect Data with Web Forms Step: New Hire Information
Data from the New Hire Information form is automatically added to the Offer Letter template, which is routed to the New Hire and the Hiring Manager for signature.
Prepare eSignature Template Step: Create Offer Letter
Send Documents for Signature Step: Send Offer Letter
If the document is signed, it should be properly stored.
If the document is not signed, the HR Representative should be notified.
Branching Rule Step:
Envelope Status = completed
True: Offer Letter is stored in Google Drive
False: HR Rep is notified
Note: Participants were included at the beginning of the workflow creation process as a best practice, but you can add participants at any point during workflow creation. Anyone who will need to take action in this workflow is a participant, and will need a defined role, based on the actions they need to take and the documents they need to use.
Complete Identity Verification
For this example, we are building the US new hire workflow. Before proceeding to the Identity Verification of the workers located in the US, we first need to differentiate US workers from workers abroad. To do that, we can use a Multi Branch Rule step.
Use Case Needs
Workflow Implementation
Different work contracts for different workers:
US Worker or International Worker
Multi Branching Rule Step:
Job Location
US, Other, No Conditions Met
If the New Hire is located in the US, their identity should be verified.
Set Up Invite Step: Invite New Hire to verify their identity
Verify Someone's Identity Step
If the New Hire is located abroad, the local HR partner should be notified.
Send an Email Step: Local HR partner is notified
If the worker's location can not be identified, the HR Representative should be notified.
Send an Email Step: HR Rep is notified the workflow failed
Best Practice
Save your workflow draft as you add steps to it. Your draft is not automatically saved.
Sign Employment Contract
At the last stage, new hires should be able to sign their work contracts based on their job designation. A Multi Branch Rule step will be used, so different paths can be created.
Use Case Needs
Workflow Implementation
If the identity verification is successful, the contracts should be routed by Job Designation.
If the identity verification fails, the HR Representative should be notified.
Branching Rule Step: Validated = True
True: Multi Branch Rule Step - Job Designation
Remote, In Office, No Conditions Met
False: Send an Email Step - HR Rep is notified IDV failed
If the New Hire is a remote worker, they should receive the contract for remote workers.
Prepare eSignature Template Step: Remote Packet
Send Documents for Signature Step: Remote Packet
If the New Hire will work in office, they should receive the contract for in-office workers.
Prepare eSignature Template Step: In Office Packet
Send Documents for Signature Step: In Office Packet
If the worker's designation can not be identified, the HR Representative should be notified.
Send an Email Step: HR Rep is notified that the workflow failed
Review and Publish
When a workflow has been completed and is ready for deployment, the final step is to Review and Publish it, by clicking Review & Publish.
The system will check for errors, which you must resolve before publishing. You can define the naming convention of your workflow instances to ensure it meets all your requirements.
Once a workflow is published, it becomes available to anyone on your account with the proper workflow permissions.

Build Agreement Workflows with Docusign
Introduction to Docusign Workflow Builder
Workflow Setup
Workflow Components
Create Workflows
Use and Manage Workflows
Lesson 4 - Create Workflows
Use and Manage Workflows
Objective: After reviewing this topic, you will be able to initiate workflows and manage running instances.
All users with Workflow Prepare permissions can initiate workflows published to your account.
Users with Workflow Create permissions can edit and republish any workflows that they have created.
Initiate a Workflow
Depending on which start method you used when creating your workflow, you will initiate the workflow in different ways.
MANUALLY TRIGGERED
AUTOMATICALLY TRIGGERED
Workflows can start from an action that is performed manually.
From a link: Someone opens a URL, and this starts the workflow. Choose this method for workflows that will be initiated by a participant, such as embedding a link on a website or in an automatic email response.
Manually in Docusign: Someone starts the workflow in the Workflow Builder. Choose this method for workflows that will be initiated by someone in your organization, such as a rental application process.
Learn More
Visit Docusign Support to learn more about using these start methods.
Run Workflow
For workflows starting manually in Docusign, click the three dots next to the desired workflow and choose Run Workflow. Anyone in your organization with Workflows: Prepare permissions will see all published workflows and can start workflows with this method. This method is similar to using a template where you populate recipient information and trigger the process, such as sending a rental application to an approved tenant.
Use Link
For workflows starting from a link, click the link icon next to the workflow to copy the URL and embed it in a website or automated email reply. This method is recommended for self-service forms such account change requests or client intake forms.
Manage Existing Workflows
Process Builders can manage any workflows they have created. The managing actions include:
Edit
Edit any of your saved drafts, published, paused, or unpublished workflows. You can add steps, modify steps, adjust participants, or change the workflow name.
If you Edit the participants or workflow steps, current active instances will not be modified, but new instances will reflect your changes.
Pause Instances
Any active instances will continue to run but no new instances can be initiated. Note:
A workflow that has been paused counts toward your workflow quota.
Changes made to a paused workflow can not be published.
A paused workflow can be resumed at any time.
Unpublish
If you are not using a workflow and you want to free up your workflow capacity, you can unpublish it, and it will remain in your account. Note:
You can only unpublish a workflow that has been paused.
No instances should be running to unpublish a workflow.
Unpublished workflows do not count toward your workflow quota.
An unpublished workflow can be published at any time.
Delete
You can permanently delete any workflow that has been unpublished. Note that you cannot recover a deleted workflow.
Export and Import
Exporting and importing a workflow allows you to move workflows or copies between accounts and environments. Note:
Step details and configurations are preserved in the export and import processes.
Any resources referenced in the steps are added to the account when the workflow is imported. This includes Web Forms and eSignature Templates.
All field mappings configured in the workflow steps are preserved.
Best Practices
Create and test new workflows in your demo account, export them, and then import the workflows into the production environment.
Export a workflow to make a new version or share with another Docusign user to preserve the current version of your workflow.
View Activity Log
Activity Logs provide full visibility into all actions taken across your workflows.
Manage Running Instances
Users with both Create and Use permissions can take the following actions:
View running instances - From the Workflows tab, click the Actions menu and select View Details to see all running, completed, and canceled instances of the workflow.
View instance details - From the Workflows page, click View Instances, then click View details next to the desired instance. This shows which steps have been completed, which step is active, and which steps are incomplete. Click View Details on a step to view additional details, such as participant name, completed date and time, and step ID.
Cancel an instance - From the instance view, click the Actions menu next to an instance and select Cancel. Data collected up to this point will be stored, but no further workflow steps will be triggered.

Build Agreement Workflows with Docusign
Introduction to Docusign Workflow Builder
Workflow Setup
Workflow Components
Create Workflows
Use and Manage Workflows
Create Workflows
Objective: After reviewing this topic, you will be able to create and publish a workflow.
You can build workflows_from a new canvas, from a workflow template, from an eSignature template, from a Web Form, or by importing a workflow.
Onboarding Use Case
Let's look at an example of an end-to-end workflow that focuses on streamlining the new hire onboarding process at a global company.
Before implementing Docusign Workflow Builder, our Human Resources teams navigated a manual, slow, and often overwhelming new hire onboarding experience. HR representatives were responsible for manually forwarding various documents for signature based on new hire responses, such as location and type of contract, and then tracking their completion.
With Workflow Builder, we've successfully automated the onboarding experience. This has significantly saved HR representatives' time, enabled automatic status updates to all relevant parties, and ensured all documents are organized and securely stored.
Paul, Human Resources Manager
For this onboarding process, an offer letter must be generated, signed, and stored. Once that is done, workers should have their identity verified before signing their specific employment contracts, which will be based on their location (US or other) and job designation (remote or in-office). At any time, if a step is not completed by the new hire, the HR representative should be notified.
This example will focus on fully building the US new hire workflow. Workers based outside the US will be directed to their local Human Resources.
The solution for this use case can be automated through Workflow Builder in three stages:
1
Generate the Offer Letter
Collect New Hire information, use it to generate the offer letter, have it routed for signatures, and store it in Google Drive.
2
Complete Identity Verification
Verify the identity of workers located in the US and notify local Human Resources partners of international workers.
3
Sign Employment Contract
Based on the job designation (remote or in-office), contracts should be routed for signature.
Note: A workflow setup is required, which includes preparing any Web Forms or eSiganature Templates. For this use case, the New Hire Information Web Form should be created, as well as the Templates for the Offer Letter and Employment Contract.
Once you have identified all the components your workflow will need, you are ready to begin. From the Agreements tab, click Workflows in the menu, then click Create Workflow.
Generate the Offer Letter
In the first stage of the workflow, you will collect the relevant participant data and generate the offer letter for signature.
Use Case Needs
Workflow Implementation
Workflow Start
Include Participants: New Hire, HR Representative, Hiring Manager
Choose starting method:
Manually in Docusign
The HR Representative
receives and completes the New Hire Information form.
Collect Data with Web Forms Step: New Hire Information
Data from the New Hire Information form is automatically added to the Offer Letter template, which is routed to the New Hire and the Hiring Manager for signature.
Prepare eSignature Template Step: Create Offer Letter
Send Documents for Signature Step: Send Offer Letter
If the document is signed, it should be properly stored.
If the document is not signed, the HR Representative should be notified.
Branching Rule Step:
Envelope Status = completed
True: Offer Letter is stored in Google Drive
False: HR Rep is notified
Note: Participants were included at the beginning of the workflow creation process as a best practice, but you can add participants at any point during workflow creation. Anyone who will need to take action in this workflow is a participant, and will need a defined role, based on the actions they need to take and the documents they need to use.
Complete Identity Verification
For this example, we are building the US new hire workflow. Before proceeding to the Identity Verification of the workers located in the US, we first need to differentiate US workers from workers abroad. To do that, we can use a Multi Branch Rule step.
Use Case Needs
Workflow Implementation
Different work contracts for different workers:
US Worker or International Worker
Multi Branching Rule Step:
Job Location
US, Other, No Conditions Met
If the New Hire is located in the US, their identity should be verified.
Set Up Invite Step: Invite New Hire to verify their identity
Verify Someone's Identity Step
If the New Hire is located abroad, the local HR partner should be notified.
Send an Email Step: Local HR partner is notified
If the worker's location can not be identified, the HR Representative should be notified.
Send an Email Step: HR Rep is notified the workflow failed
Best Practice
Save your workflow draft as you add steps to it. Your draft is not automatically saved.
Sign Employment Contract
At the last stage, new hires should be able to sign their work contracts based on their job designation. A Multi Branch Rule step will be used, so different paths can be created.
Use Case Needs
Workflow Implementation
If the identity verification is successful, the contracts should be routed by Job Designation.
If the identity verification fails, the HR Representative should be notified.
Branching Rule Step: Validated = True
True: Multi Branch Rule Step - Job Designation
Remote, In Office, No Conditions Met
False: Send an Email Step - HR Rep is notified IDV failed
If the New Hire is a remote worker, they should receive the contract for remote workers.
Prepare eSignature Template Step: Remote Packet
Send Documents for Signature Step: Remote Packet
If the New Hire will work in office, they should receive the contract for in-office workers.
Prepare eSignature Template Step: In Office Packet
Send Documents for Signature Step: In Office Packet
If the worker's designation can not be identified, the HR Representative should be notified.
Send an Email Step: HR Rep is notified that the workflow failed
Review and Publish
When a workflow has been completed and is ready for deployment, the final step is to Review and Publish it, by clicking Review & Publish.
The system will check for errors, which you must resolve before publishing. You can define the naming convention of your workflow instances to ensure it meets all your requirements.
Once a workflow is published, it becomes available to anyone on your account with the proper workflow permissions.
Use and Manage Workflows
Objective: After reviewing this topic, you will be able to initiate workflows and manage running instances.
All users with Workflow Prepare permissions can initiate workflows published to your account.
Users with Workflow Create permissions can edit and republish any workflows that they have created.
Initiate a Workflow
Depending on which start method you used when creating your workflow, you will initiate the workflow in different ways.
MANUALLY TRIGGERED
AUTOMATICALLY TRIGGERED
Workflows can start from an action that is performed manually.
From a link: Someone opens a URL, and this starts the workflow. Choose this method for workflows that will be initiated by a participant, such as embedding a link on a website or in an automatic email response.
Manually in Docusign: Someone starts the workflow in the Workflow Builder. Choose this method for workflows that will be initiated by someone in your organization, such as a rental application process.
Learn More
Visit Docusign Support to learn more about using these start methods.
Run Workflow
For workflows starting manually in Docusign, click the three dots next to the desired workflow and choose Run Workflow. Anyone in your organization with Workflows: Prepare permissions will see all published workflows and can start workflows with this method. This method is similar to using a template where you populate recipient information and trigger the process, such as sending a rental application to an approved tenant.
Use Link
For workflows starting from a link, click the link icon next to the workflow to copy the URL and embed it in a website or automated email reply. This method is recommended for self-service forms such account change requests or client intake forms.
Manage Existing Workflows
Process Builders can manage any workflows they have created. The managing actions include:
Edit
Edit any of your saved drafts, published, paused, or unpublished workflows. You can add steps, modify steps, adjust participants, or change the workflow name.
If you Edit the participants or workflow steps, current active instances will not be modified, but new instances will reflect your changes.
Pause Instances
Any active instances will continue to run but no new instances can be initiated. Note:
A workflow that has been paused counts toward your workflow quota.
Changes made to a paused workflow can not be published.
A paused workflow can be resumed at any time.
Unpublish
If you are not using a workflow and you want to free up your workflow capacity, you can unpublish it, and it will remain in your account. Note:
You can only unpublish a workflow that has been paused.
No instances should be running to unpublish a workflow.
Unpublished workflows do not count toward your workflow quota.
An unpublished workflow can be published at any time.
Delete
You can permanently delete any workflow that has been unpublished. Note that you cannot recover a deleted workflow.
Export and Import
Exporting and importing a workflow allows you to move workflows or copies between accounts and environments. Note:
Step details and configurations are preserved in the export and import processes.
Any resources referenced in the steps are added to the account when the workflow is imported. This includes Web Forms and eSignature Templates.
All field mappings configured in the workflow steps are preserved.
Best Practices
Create and test new workflows in your demo account, export them, and then import the workflows into the production environment.
Export a workflow to make a new version or share with another Docusign user to preserve the current version of your workflow.
View Activity Log
Activity Logs provide full visibility into all actions taken across your workflows.
Manage Running Instances
Users with both Create and Use permissions can take the following actions:
View running instances - From the Workflows tab, click the Actions menu and select View Details to see all running, completed, and canceled instances of the workflow.
View instance details - From the Workflows page, click View Instances, then click View details next to the desired instance. This shows which steps have been completed, which step is active, and which steps are incomplete. Click View Details on a step to view additional details, such as participant name, completed date and time, and step ID.
Cancel an instance - From the instance view, click the Actions menu next to an instance and select Cancel. Data collected up to this point will be stored, but no further workflow steps will be triggered.
Lesson 5 - Use and Manage Workflows

## Docusign Web Forms API

### Create Forms to Enhance the Signing Experience 25 min

Create Forms to Enhance the Signing Experience
Introduction to Docusign Forms
CREATE AND MANAGE WEB FORMS
Create Web Forms
Manage Web Forms
Knowledge Check
Lesson 5 - Manage Web Forms
Knowledge Check
When is a standalone Web Form typically used?
When you need to collect data and require a signature.
When you want to use a Web Form as part of a Workflow.
Only when you are using the Web Forms API.
When you have an existing eSignature template.
SUBMIT
Incorrect
A standalone Web Form is typically used when you want to use a Web Form as part of a Maestro workflow.
TAKE AGAIN
What is the purpose of "Descriptive Data Labels" in an envelope template used for a Web Form?
To control the appearance of the Web Form.
To ensure clear identification of fields within the Web Form builder.
To automatically populate fields with signer information.
SUBMIT
Incorrect
The purpose of "Descriptive Data Labels" in an envelope template is to ensure clear identification of fields within the Web Form builder.
TAKE AGAIN
What happens when you import an envelope template into the Web Forms builder?
The original eSignature template is modified.
A copy of the template, called a Web Form template, is created.
The template is directly converted into a PDF.
The template is deleted from the system.
SUBMIT
Incorrect
When you import an eSignature template into the Web Form builder a copy of the template, called a Web Form template, is created.
TAKE AGAIN
What is the primary function of conditional rules in Docusign Web Forms?
To validate the data entered by the signer.
To control the layout of the Web Form.
To personalize the signing experience based on signer responses.
SUBMIT
Incorrect
The primary function of conditional rules in Docusign Web Forms is to personalize the signing experience based on signer responses.
TAKE AGAIN

Create Forms to Enhance the Signing Experience
RESUME COURSE
Welcome to the Create Forms to Enhance the Signing Experience course. After reviewing this course, you will be able to:
Create and manage Docusign Web Forms.
Recommended Prerequisites:
Create Docusign Templates to Simplify Sending
Introduction to Docusign Forms
CREATE AND MANAGE WEB FORMS
Create Web Forms
Manage Web Forms
Knowledge Check

## Docusign Agreement Manager API

### Docusign Agreement Manager for Business Users 30 min

_UI-only content (finding and sharing agreements) removed as out of exam scope. For API-relevant Agreement Manager topics, see "Exam Gap Topics > Section 6" at the end of this file._

### Docusign Agreement Manager for Administrators 60 min

Docusign Agreement Manager for Administrators
Access Management
Import Agreements
Agreement Types
Parties and Obligations
Dashboards, Insights, and Renewals
Lesson 3 - Agreement Types
Parties and Obligations
Objective: After reviewing this topic, you will be able to review and manage agreement parties and obligations.
A party in an agreement refers to an individual, company, or organization that is legally bound by the terms of the agreement. When agreements are added to Agreement Manager, key data points such as party names are automatically surfaced to help you identify who is involved in each agreement. A party could be a customer in sales or a vendor in procurement. Managing parties allows you to quickly find agreements linked to each party.
Navigate the Parties Page
→ From the Agreements page, click Parties in the left panel.
I need to quickly identify all agreements that are nearing expiration for Fontara, one of the customers I oversee.
To do this, I navigate to the Parties page in Agreement Manager and search for Fontara. I select Fontara from the list, and the party hub loads. The party hub is a unified summary of all agreements and obligations associated with Fontara.
Paul, Contract Manager at Stellar Logical Software
Select Fontara from the Parties page.
Manage Parties
Setting the party as internal or external.
Merging duplicate parties that use different variations of the same name.
Manually merging parties that were not flagged as duplicates.
Unmerging parties merged by mistake.
On the Manage Parties page, each party is identified as internal or external. This designation gives you the context needed to manage relationships, risks, and obligations.
As Docusign Iris captures party names from agreements, slight name variations may result in duplicate party names. Through duplicate party management, you can merge duplicate parties into a single preferred name.
After merging parties, it may take up to an hour for the changes to reflect in the Agreements and Reports pages.
View and Manage Obligations
Obligations are the actions or commitments that one or more parties agree to fulfill as part of an agreement. They are made up of attributes and extracted contractual data contained within clauses across one or multiple documents. With obligation management, contract administrators can take a proactive approach to ensuring that contract commitments are captured, tracked, and fulfilled.
Agreement Manager automatically surfaces certain obligation types with AI, while also allowing you to manually create additional obligations as needed. By tracking these obligations, you have visibility into the required actions and support compliance.
Surface Obligations with Docusign Iris
Docusign Iris processes your agreements to extract key attributes, including payment, renewal, and termination obligations, so you can effectively capture, track, and fulfill them. The attributes for these obligation types are extracted when they are present in the agreement.
Obligation Type
Obligation Name
Payment
One-Time Payment
Deposit Payment
Renewal
Renewal Notice
Termination
Termination for Cause Notice
Termination for Convenience Notice
View Obligations in an Agreement
You can view the obligations for a specific agreement by opening an agreement from the Completed page.
Select the Obligations tab in the agreement preview.
In this example, you can verify that an obligation for a Termination for Convenience Notice was surfaced by AI. Click the obligation to view the details.
The extracted obligation attributes from the agreement are displayed. Review the attribute values. Click the spark (*) icon to review the attribute against the data in the agreement.
View the Obligations for a Party
Navigate to Parties and then select a party to access a summary of the agreements and obligations associated with the party.
Click the Obligations tab, and all obligations related to the party are listed.
Select an obligation to open the obligation details in the agreement preview.
Review the attribute values.
View Obligations for a Party
Note: View the complete list of obligation types and extracted attributes for obligations surfaced with AI and manually created obligations in the Obligation Management
support article.
Create an Obligation
In addition to the payment, renewal, and termination obligation types extracted by AI, you can manually create and add other types of obligations to the agreement.
From the agreement preview, select the Obligations to review existing obligations. You can select an obligation to view the additional details.
To create a new obligation, highlight the specific clause that you would like to create an obligation for. Select Create Obligation.
Complete and save the details of the obligation. The new obligation is added to the Obligations.
Note: Review the Manually Create an Obligation
support article for guidance on completing the obligation fields.
Assign an Obligation
As a contract administrator, you can assign obligations to other users or team members to ensure clear ownership, accountability, and ongoing compliance with the agreement's requirements.
Assign an obligation
After reviewing the list of obligations for an agreement, select the obligation to assign. Update the Owner field by entering the name or the email address of the assignee and selecting the user from the prompted list. Save the changes.
The obligation owner information can be used as a filter in the Obligations dashboard, allowing you to view obligations assigned to a specific user. You'll learn more about working with dashboards and reports in the next lesson.
Manage Obligation Types
You've seen that standard obligation types are available for both AI-assisted and manually created obligations. However, you can also create custom obligation types to categorize your obligations more accurately.
From the Completed page, select the gear icon and then select Obligations.
The list of standard obligation types indicates that they were created by Docusign. Create a new obligation type.
Enter a name for the custom obligation type and then save. The new type is added as a User-created obligation type. The custom type can now be used when editing or creating an obligation.
Lesson 5 - Dashboards, Insights, and Renewals

Docusign Agreement Manager for Administrators
Welcome to the Docusign Agreement Manager for Administrators course. After reviewing this course, you will be able to:
Manage Agreement Manager access for users and groups.
Import agreements to Agreement Manager.
Manage agreement types and custom extractions.
Review and manage agreement parties.
Create, view, and manage obligations.
Ensure compliance through IAM dashboards and reports
Manage renewals.
Access Management
Import Agreements
Agreement Types
Parties and Obligations
Dashboards, Insights, and Renewals

Docusign Agreement Manager for Administrators
Access Management
Import Agreements
Agreement Types
Parties and Obligations
Dashboards, Insights, and Renewals
Agreement Types
Objective: After reviewing this topic, you will be able to manage agreement types and their associated custom fields for use in custom extractions.
Each agreement that is uploaded into Agreement Manager is assigned an agreement type. You have likely already seen agreement types such as a Statement of Work or Non-Disclosure Agreement.
Using Agreement Types and Standard Fields
An agreement type classifies agreements and identifies important fields relevant to each type. Each agreement type includes a defined set of standard fields or attributes that are extracted and used to search, filter, and analyze agreements.
For example, if a Fontara Statement of Work has a similar structure and language as other existing Statements of Work, Agreement Manager will likely classify it under the Statement of Work agreement type. Since this agreement type typically includes an Effective Date field, the repository searches for that date within the agreement. If no effective date is found, there is no value assigned to the Effective Date agreement attribute. A business user can then review the agreement and manually update the Effective Date attribute field.
Agreement Types and Standard Fields
Note: Your account plan may not support all features and options discussed in this course. Visit our Get Support
page for contact options if you need assistance, or to search for information on specific features.
Manage Custom Extractions
Custom extractions are a way to customize Agreement Manager to obtain additional organization and industry-specific agreement information beyond the standard Docusign-provided fields. Custom extractions may include custom agreement types, as well as custom fields.
When you enable AI for custom agreement types or custom fields, this additional data is surfaced in your agreements. Custom extractions offer the following benefits:
Better visibility into your agreements and the values contained within them
Enhanced compliance tracking with customized values that are specific to a particular agreement type
Increased organization-wide productivity by tracking information that is unique to your organization or industry
CUSTOM EXTRACTIONS USE CASE
Robin Meyer tracks international shipments and their associated contracts for a major global ocean transport corporation to ensure the organization is in compliance with multiple governmental regulatory agencies.
Often, Robin has to manually review each shipping contract to obtain the name of the vessel, the type of cargo, and any import-export fees, as well as the ship's captain and their contact information for each shipment.
There is no shipping contract standard agreement type, and none of these values are captured using any standard Docusign agreement types.
Therefore, to maximize his productivity and efficiency, Robin creates a custom agreement type of Shipping Contract. He then trains AI to identify agreements that should be categorized as shipping contracts.
Robin then adds the following custom fields to the Shipping Contract custom agreement type and enables AI to locate and extract these attribute values from agreements:
Vessel Name
Type of Cargo
Import Fee
Export Fee
Name of Ship's Captain
Ship's Captain Cell Phone
Ship's Captain Email Address
Now, Robin can run reports and categorize agreements based on the custom fields he has added to the Shipping Contract custom agreement type.
Custom Extractions and Field Detection
Create a Custom Agreement Type
Custom agreement types capture specific, unique information that is not covered by standard agreement fields and agreement types. Administrators can use custom agreement types and fields to tailor their contracts to fit the exact needs of different customers.
If Agreement Manager is unable to determine the agreement type during upload, the system assigns the type as Other.
You can create custom agreement types to limit the number of agreements classified as Other to help you manage your agreements.
Note: When creating a new agreement type, you can:
Select which fields to associate with it.
Set up, activate, and test the accuracy of AI detection for the new agreement type.
Manage Custom Fields
Every agreement type is associated with a list of fields that capture relevant, specific, and unique information.
In some cases, you may want to capture information that isn't covered by the standard fields associated with the agreement type. For these instances, you can add custom fields to both standard and custom agreement types to match specific business use cases.
Note: After adding a field to an agreement type, enable AI to automatically detect and surface the value of the custom field from agreements.
Docusign University
Continue learning about the topics covered in this course. Search Docusign University to explore recommended content listed below. Click the link for your account type to register. (Customer
| Developer/Demo
| Employee
| Partner
)
Docusign Agreement Manager for Business Users
Docusign IAM: Install Apps from Docusign App Center
Docusign for Salesforce: Access Agreement Manager Agreement Insights
Additional Resources
Docusign Support
Docusign Community
Docusign on YouTube
Docusign Developer Center
Docusign IAM Platform
Create, commit to, and manage your agreements all in one collaborative platform.
What is the IAM Platform?
Docusign Certifications
Distinguish yourself as a Docusign expert by demonstrating your skills and experience with Docusign products and solutions.
Visit our certifications page or watch the video below to learn more about getting Docusign Certified. (Customers
| Developers
| Employees
| Partners
)
Lesson 4 - Parties and Obligations

Docusign Agreement Manager for Administrators
Access Management
Import Agreements
Agreement Types
Parties and Obligations
Dashboards, Insights, and Renewals
Parties and Obligations
Objective: After reviewing this topic, you will be able to review and manage agreement parties and obligations.
A party in an agreement refers to an individual, company, or organization that is legally bound by the terms of the agreement. When agreements are added to Agreement Manager, key data points such as party names are automatically surfaced to help you identify who is involved in each agreement. A party could be a customer in sales or a vendor in procurement. Managing parties allows you to quickly find agreements linked to each party.
Navigate the Parties Page
→ From the Agreements page, click Parties in the left panel.
I need to quickly identify all agreements that are nearing expiration for Fontara, one of the customers I oversee.
To do this, I navigate to the Parties page in Agreement Manager and search for Fontara. I select Fontara from the list, and the party hub loads. The party hub is a unified summary of all agreements and obligations associated with Fontara.
Paul, Contract Manager at Stellar Logical Software
Select Fontara from the Parties page.
Manage Parties
Setting the party as internal or external.
Merging duplicate parties that use different variations of the same name.
Manually merging parties that were not flagged as duplicates.
Unmerging parties merged by mistake.
On the Manage Parties page, each party is identified as internal or external. This designation gives you the context needed to manage relationships, risks, and obligations.
As Docusign Iris captures party names from agreements, slight name variations may result in duplicate party names. Through duplicate party management, you can merge duplicate parties into a single preferred name.
After merging parties, it may take up to an hour for the changes to reflect in the Agreements and Reports pages.
View and Manage Obligations
Obligations are the actions or commitments that one or more parties agree to fulfill as part of an agreement. They are made up of attributes and extracted contractual data contained within clauses across one or multiple documents. With obligation management, contract administrators can take a proactive approach to ensuring that contract commitments are captured, tracked, and fulfilled.
Agreement Manager automatically surfaces certain obligation types with AI, while also allowing you to manually create additional obligations as needed. By tracking these obligations, you have visibility into the required actions and support compliance.
Surface Obligations with Docusign Iris
Docusign Iris processes your agreements to extract key attributes, including payment, renewal, and termination obligations, so you can effectively capture, track, and fulfill them. The attributes for these obligation types are extracted when they are present in the agreement.
Obligation Type
Obligation Name
Payment
One-Time Payment
Deposit Payment
Renewal
Renewal Notice
Termination
Termination for Cause Notice
Termination for Convenience Notice
View Obligations in an Agreement
You can view the obligations for a specific agreement by opening an agreement from the Completed page.
Select the Obligations tab in the agreement preview.
In this example, you can verify that an obligation for a Termination for Convenience Notice was surfaced by AI. Click the obligation to view the details.
The extracted obligation attributes from the agreement are displayed. Review the attribute values. Click the spark (*) icon to review the attribute against the data in the agreement.
View the Obligations for a Party
Navigate to Parties and then select a party to access a summary of the agreements and obligations associated with the party.
Click the Obligations tab, and all obligations related to the party are listed.
Select an obligation to open the obligation details in the agreement preview.
Review the attribute values.
View Obligations for a Party
Note: View the complete list of obligation types and extracted attributes for obligations surfaced with AI and manually created obligations in the Obligation Management
support article.
Create an Obligation
In addition to the payment, renewal, and termination obligation types extracted by AI, you can manually create and add other types of obligations to the agreement.
From the agreement preview, select the Obligations to review existing obligations. You can select an obligation to view the additional details.
To create a new obligation, highlight the specific clause that you would like to create an obligation for. Select Create Obligation.
Complete and save the details of the obligation. The new obligation is added to the Obligations.
Note: Review the Manually Create an Obligation
support article for guidance on completing the obligation fields.
Assign an Obligation
As a contract administrator, you can assign obligations to other users or team members to ensure clear ownership, accountability, and ongoing compliance with the agreement's requirements.
Assign an obligation
After reviewing the list of obligations for an agreement, select the obligation to assign. Update the Owner field by entering the name or the email address of the assignee and selecting the user from the prompted list. Save the changes.
The obligation owner information can be used as a filter in the Obligations dashboard, allowing you to view obligations assigned to a specific user. You'll learn more about working with dashboards and reports in the next lesson.
Manage Obligation Types
You've seen that standard obligation types are available for both AI-assisted and manually created obligations. However, you can also create custom obligation types to categorize your obligations more accurately.
From the Completed page, select the gear icon and then select Obligations.
The list of standard obligation types indicates that they were created by Docusign. Create a new obligation type.
Enter a name for the custom obligation type and then save. The new type is added as a User-created obligation type. The custom type can now be used when editing or creating an obligation.
Agreement Types
Objective: After reviewing this topic, you will be able to manage agreement types and their associated custom fields for use in custom extractions.
Each agreement that is uploaded into Agreement Manager is assigned an agreement type. You have likely already seen agreement types such as a Statement of Work or Non-Disclosure Agreement.
Using Agreement Types and Standard Fields
An agreement type classifies agreements and identifies important fields relevant to each type. Each agreement type includes a defined set of standard fields or attributes that are extracted and used to search, filter, and analyze agreements.
For example, if a Fontara Statement of Work has a similar structure and language as other existing Statements of Work, Agreement Manager will likely classify it under the Statement of Work agreement type. Since this agreement type typically includes an Effective Date field, the repository searches for that date within the agreement. If no effective date is found, there is no value assigned to the Effective Date agreement attribute. A business user can then review the agreement and manually update the Effective Date attribute field.
Agreement Types and Standard Fields
Note: Your account plan may not support all features and options discussed in this course. Visit our Get Support
page for contact options if you need assistance, or to search for information on specific features.
Manage Custom Extractions
Custom extractions are a way to customize Agreement Manager to obtain additional organization and industry-specific agreement information beyond the standard Docusign-provided fields. Custom extractions may include custom agreement types, as well as custom fields.
When you enable AI for custom agreement types or custom fields, this additional data is surfaced in your agreements. Custom extractions offer the following benefits:
Better visibility into your agreements and the values contained within them
Enhanced compliance tracking with customized values that are specific to a particular agreement type
Increased organization-wide productivity by tracking information that is unique to your organization or industry
CUSTOM EXTRACTIONS USE CASE
Robin Meyer tracks international shipments and their associated contracts for a major global ocean transport corporation to ensure the organization is in compliance with multiple governmental regulatory agencies.
Often, Robin has to manually review each shipping contract to obtain the name of the vessel, the type of cargo, and any import-export fees, as well as the ship's captain and their contact information for each shipment.
There is no shipping contract standard agreement type, and none of these values are captured using any standard Docusign agreement types.
Therefore, to maximize his productivity and efficiency, Robin creates a custom agreement type of Shipping Contract. He then trains AI to identify agreements that should be categorized as shipping contracts.
Robin then adds the following custom fields to the Shipping Contract custom agreement type and enables AI to locate and extract these attribute values from agreements:
Vessel Name
Type of Cargo
Import Fee
Export Fee
Name of Ship's Captain
Ship's Captain Cell Phone
Ship's Captain Email Address
Now, Robin can run reports and categorize agreements based on the custom fields he has added to the Shipping Contract custom agreement type.
Custom Extractions and Field Detection
Create a Custom Agreement Type
Custom agreement types capture specific, unique information that is not covered by standard agreement fields and agreement types. Administrators can use custom agreement types and fields to tailor their contracts to fit the exact needs of different customers.
If Agreement Manager is unable to determine the agreement type during upload, the system assigns the type as Other.
You can create custom agreement types to limit the number of agreements classified as Other to help you manage your agreements.
Note: When creating a new agreement type, you can:
Select which fields to associate with it.
Set up, activate, and test the accuracy of AI detection for the new agreement type.
Manage Custom Fields
Every agreement type is associated with a list of fields that capture relevant, specific, and unique information.
In some cases, you may want to capture information that isn't covered by the standard fields associated with the agreement type. For these instances, you can add custom fields to both standard and custom agreement types to match specific business use cases.
Note: After adding a field to an agreement type, enable AI to automatically detect and surface the value of the custom field from agreements.
Lesson 5 - Dashboards, Insights, and Renewals

Docusign Agreement Manager for Administrators
Access Management
Import Agreements
Agreement Types
Parties and Obligations
Dashboards, Insights, and Renewals
Parties and Obligations
Objective: After reviewing this topic, you will be able to review and manage agreement parties and obligations.
A party in an agreement refers to an individual, company, or organization that is legally bound by the terms of the agreement. When agreements are added to Agreement Manager, key data points such as party names are automatically surfaced to help you identify who is involved in each agreement. A party could be a customer in sales or a vendor in procurement. Managing parties allows you to quickly find agreements linked to each party.
Navigate the Parties Page
→ From the Agreements page, click Parties in the left panel.
I need to quickly identify all agreements that are nearing expiration for Fontara, one of the customers I oversee.
To do this, I navigate to the Parties page in Agreement Manager and search for Fontara. I select Fontara from the list, and the party hub loads. The party hub is a unified summary of all agreements and obligations associated with Fontara.
Paul, Contract Manager at Stellar Logical Software
Select Fontara from the Parties page.
Manage Parties
Setting the party as internal or external.
Merging duplicate parties that use different variations of the same name.
Manually merging parties that were not flagged as duplicates.
Unmerging parties merged by mistake.
On the Manage Parties page, each party is identified as internal or external. This designation gives you the context needed to manage relationships, risks, and obligations.
As Docusign Iris captures party names from agreements, slight name variations may result in duplicate party names. Through duplicate party management, you can merge duplicate parties into a single preferred name.
After merging parties, it may take up to an hour for the changes to reflect in the Agreements and Reports pages.
View and Manage Obligations
Obligations are the actions or commitments that one or more parties agree to fulfill as part of an agreement. They are made up of attributes and extracted contractual data contained within clauses across one or multiple documents. With obligation management, contract administrators can take a proactive approach to ensuring that contract commitments are captured, tracked, and fulfilled.
Agreement Manager automatically surfaces certain obligation types with AI, while also allowing you to manually create additional obligations as needed. By tracking these obligations, you have visibility into the required actions and support compliance.
Surface Obligations with Docusign Iris
Docusign Iris processes your agreements to extract key attributes, including payment, renewal, and termination obligations, so you can effectively capture, track, and fulfill them. The attributes for these obligation types are extracted when they are present in the agreement.
Obligation Type
Obligation Name
Payment
One-Time Payment
Deposit Payment
Renewal
Renewal Notice
Termination
Termination for Cause Notice
Termination for Convenience Notice
View Obligations in an Agreement
You can view the obligations for a specific agreement by opening an agreement from the Completed page.
Select the Obligations tab in the agreement preview.
In this example, you can verify that an obligation for a Termination for Convenience Notice was surfaced by AI. Click the obligation to view the details.
The extracted obligation attributes from the agreement are displayed. Review the attribute values. Click the spark (*) icon to review the attribute against the data in the agreement.
View the Obligations for a Party
Navigate to Parties and then select a party to access a summary of the agreements and obligations associated with the party.
Click the Obligations tab, and all obligations related to the party are listed.
Select an obligation to open the obligation details in the agreement preview.
Review the attribute values.
View Obligations for a Party
Note: View the complete list of obligation types and extracted attributes for obligations surfaced with AI and manually created obligations in the Obligation Management
support article.
Create an Obligation
In addition to the payment, renewal, and termination obligation types extracted by AI, you can manually create and add other types of obligations to the agreement.
From the agreement preview, select the Obligations to review existing obligations. You can select an obligation to view the additional details.
To create a new obligation, highlight the specific clause that you would like to create an obligation for. Select Create Obligation.
Complete and save the details of the obligation. The new obligation is added to the Obligations.
Note: Review the Manually Create an Obligation
support article for guidance on completing the obligation fields.
Assign an Obligation
As a contract administrator, you can assign obligations to other users or team members to ensure clear ownership, accountability, and ongoing compliance with the agreement's requirements.
Assign an obligation
After reviewing the list of obligations for an agreement, select the obligation to assign. Update the Owner field by entering the name or the email address of the assignee and selecting the user from the prompted list. Save the changes.
The obligation owner information can be used as a filter in the Obligations dashboard, allowing you to view obligations assigned to a specific user. You'll learn more about working with dashboards and reports in the next lesson.
Manage Obligation Types
You've seen that standard obligation types are available for both AI-assisted and manually created obligations. However, you can also create custom obligation types to categorize your obligations more accurately.
From the Completed page, select the gear icon and then select Obligations.
The list of standard obligation types indicates that they were created by Docusign. Create a new obligation type.
Enter a name for the custom obligation type and then save. The new type is added as a User-created obligation type. The custom type can now be used when editing or creating an obligation.
Dashboards, Insights, and Renewals
Objective: After reviewing this topic, you will be able to use the IAM dashboards and reports to keep track of important agreement data, take action on insights, manage renewals, and ensure compliance.
The Insights tab provides centralized access to all reports and dashboards in Agreement Manager. From here, you can quickly view available dashboards and reports for envelopes, agreements, obligNaations, renewals, and requests, as well as create custom dashboards and reports for your organization. You can also manage subscriptions through report notifications, keeping you informed of key agreement details, actions, and obligations.
Overview
When you select Insights from the global header, you are directed to the Overview page. From here, you can:
Search for any report or custom dashboards in Agreement Manager.
Access recently viewed and starred (favorite) reports.
Review agreements that are active this month, expiring, and renewing in the next 90 days.
Explore Docusign Insights on upcoming renewals and envelope metrics like status, usage, and environmental savings.
Create custom dashboards and reports.
Insights > Overview
Dashboards
Dashboards display a collection of reports, providing a bigger picture, a visual overview, or a summary of key agreement details for quick insights.
My dashboard and Admistrator dashboard
These dashboards provide an overview of your account and your organization's envelope activities and the environmental savings associated with reduced paper use.
Agreements
The Agreements dashboard provides a visual summary of all completed agreements, offering top-level insights into actionable content, such as active agreements and those with upcoming expiration and renewal dates within the next 90 days.
VIEW THE AGREEMENTS DASHBOARD
VIEW REPORT DETAILS
MANAGE REPORT SUBSCRIPTIONS
Some navigation actions are available across the IAM dashboards and reports. You can:
Select the Favorite (star) icon to add them to your favorites on the Overview dashboard.
Use the filters to refine the dashboard, and your selection applies to all charts and reports.
Click on a chart or select View Report from the menu to view the detailed report. The report details are described in the next tab.
From the chart, you can also select:
View as table: To display the data in a table within the chart.
Download as png: To download an image of the chart to your local Downloads folder.
Best Practice
Select a bar or section from a bar, pie, or donut chart to view the agreements represented in the bar or section. The report view opens and the corresponding agreements are displayed in the table.
Obligations
The Obligations dashboard provides a visual summary of agreement obligations that were surfaced with Docusign Iris and those manually added. This dashboard includes these charts:
Obligations by due date: Displays the number of obligations due over the next six months.
Obligations by type: Displays all obligations grouped by obligation type.
Renewals
An agreement renewal is the process extending an agreement beyond its initial term. The renewal process is based on the agreement's renewal type, which specifies how the agreement can be renewed or extended. For example, an agreement with an Automatic Renewal type automatically renews at the end of its term, while an Evergreen agreement continues indefinitely unless a party decides to terminate it.
Docusign Agreement Manager helps you retrieve the agreement data needed to proactively take action on agreement renewals and terminations. Managing renewals can help your organization achieve:
Operational efficiency by providing one source of truth and automated processes to help keep your organization's employees informed of terminated or automatically renewed agreements.
Cost savings through making your users aware of upcoming renewals and terminations that must be managed. Organizations waste money when they unintentionally miss renegotiation and termination windows for expiring agreements.
Increased revenue by enabling your users to proactively reach out to customers to negotiate renewals while cutting down on unintentional agreement terminations.
Mitigating risk because renewal management helps your users stay on top of important dates and ensure compliance.
Drive Agreement Renewals Through AI-Assisted Insights
Attribute values are automatically extracted from Agreement Manager agreements. These attribute values drive insight into agreement renewals and feed data into the Renewals dashboard and the renewal email notifications. The Docusign Agreement Manager for Business Users course highlights the importance of validating agreement data by updating and reviewing AI-suggested attribute values, including renewal-related fields, so the Renewals dashboard remains accurate.
Renewals Dashboard
As contract administrators or business users, you can stay ahead of upcoming renewals by using the Renewals dashboard. By leveraging renewal attribute values extracted from agreements, the dashboard delivers a clear visual summary through the available charts and tables.
Configure Renewal Notifications
To get notified automatically when a renewal is nearing its due date, you can set up email notifications which will send you an email reminder using the frequency you choose.
Renewal Management Use Cases
The Stellar Logical Software renewals management cross-functional team is having their monthly meeting to coordinate renewals. Click the plus sign icons below to learn more about how the Stellar Logical Software renewals management team leverages Agreement Manager to help them manage agreement renewals.
DRIVE NEGOTIATIONS FOR RENEWAL
GAIN TIMELY VISIBILITY INTO UPCOMING RENEWALS
STAY INFORMED OF TIME-SENSITIVE RENEWALS
At Stellar Logical Software, Mei is a contract manager who has set up renewal email notifications so she can be alerted when a renewal is coming due in 120 days. This usually gives her enough time to renegotiate the agreements for more favorable terms.
Mei relies on the Renewals dashboard to find out what the status or relationship is of the parties included in the agreement. This also helps Mei to see when renewal notices are coming due so she can better plan workloads for herself and her staff.
Reports
The Reports section allows contract administrators to view report activities across all users in the account, while business users can review their own report activity. The available reports are grouped in tabs to quickly review recently accessed reports, standard and custom reports, and any downloaded reports.
Note: Review the information provided on envelopes, recipients, and account activities in the List of Standard Reports
. Read the Document Data Reports
to focus on field-level data in your eSignature agreements.
Create Custom Dashboards and Reports
Create reports and dashboards
While Docusign Agreement Manager offers predefined reports and dashboards to surface key agreement information, sometimes you may need to analyze specialized information such as custom extractions. With the ability to create custom dashboards and reports, you can obtain more information about your agreements, enabling more data-driven decision-making.
Custom Dashboards and Reports
Lesson 5 - Dashboards, Insights, and Renewals

## Docusign Connected Fields API and Docusign ID Evidence API

### Configure eSignature Identity Verification Preferences 20 min

Configure eSignature Identity Verification Preferences
Introduction to Identity Verification Preferences
Manage Envelopes with Authentication or Identity Verification
Manage Identity Verification Configurations
Knowledge Check
Introduction to Identity Verification Preferences
Protect your agreements and support compliance with government and industry regulations by verifying recipients' identities.
Note: Your account plan may not support the features covered in this course. Visit our Get Support
page for contact options if you need assistance, or to search for information on specific features.
Identity Verification Preferences Overview
Docusign Identify
Docusign Identify provides various options that enable you to authenticate and verify recipients' identities before they can review and sign their documents or as they complete Workflow Builder steps.
By default, recipient authentication and identity verification are not required; when users send envelopes, they choose whether or not to apply this feature for each recipient. However, as an eSignature administrator, you can require that all recipients pass an authentication or identity verification check before they can access any documents sent from the account.
Access Code Authentication
Phone Authentication
Knowledge-Based
Docusign ID Verification
Docusign ID Verification with Liveness
Docusign ID Verification with Japanese IDs
Docusign ID Verification for FINTRAC
Docusign ID Verification for IAL2
Docusign ID Verification for NYCRR500 Compliance
Docusign Risk-Based Verification
Note: The phone authentication, knowledge-based authentication, and ID Verification methods incur a per-use fee.
Digital Signatures and Signer Identity Assurance
For most use cases, customers, and locations, a standard electronic signature with or without identity verification is sufficient. However, for some transactions in heavily regulated industries, in specific regions such as the European Union, or with governmental entities, you may be required or prefer to use digital signatures.
A digital signature is an electronic signature that uses a technology called a digital certificate to authenticate the signer’s identity. Digital certificates indicate that the signers have completed extra steps to confirm their identities. A signer’s digital certificate is used to create the signature and then attached to the signed document.
The steps can range from entering a security code or going through Docusign ID Verification and accepting specific terms and conditions, to even going through a live face-to-face verification.
The Docusign platform accepts certificates from leading Trust Service Providers across the world through API integrations with our Trust Service Provider partners, other third-party integrations, and directly from signers. Docusign is also an authorized Trust Service Provider on the EU Trust List, issuing digital certificates at the Advanced and Qualified levels that support your efforts to comply with eIDAS.
Review the resources below for more information on digital signatures:
Best-practice Guide
Explore this Best-practice Guide and find more information on Standards-Based Signatures & Identity Verification.
DSU
Use Digital Certificate-Based Signatures for More Secure Agreements
Access the support page for more information on digital signatures.
Business Use Cases
Getting Started
→ From the Docusign home screen, navigate to the Admin page.
Click Security Settings to configure recipient authentication settings.
Click Identity Verification to configure phone authentication, knowledge-based authentication, and Docusign ID Verification.
update screenshot
Security Settings
From the Security Settings page, scroll down to the Authentication Settings section to set recipient authentication behavior for the entire account.
Note: These settings can be very important since most accounts are charged per authentication check.
Recipient Authentication Settings
Recipient Authentication Triggers
Recipient Authentication Skip Option
Login Requirements
General Authentication Settings
Access Codes
Lesson 2 - Manage Envelopes with Authentication or Identity Verification

Configure eSignature Identity Verification Preferences
Welcome to the Configure eSignature Identity Verification Preferences course. After reviewing this course, you will be able to:
List the solutions available within the Docusign Identify portfolio to verify your recipients' identity.
Describe the steps involved in requiring a recipient to authenticate or verify their identity.
Manage the identity verification configurations available to your users.
Introduction to Identity Verification Preferences
Manage Envelopes with Authentication or Identity Verification
Manage Identity Verification Configurations
Knowledge Check

Configure eSignature Identity Verification Preferences
Introduction to Identity Verification Preferences
Manage Envelopes with Authentication or Identity Verification
Manage Identity Verification Configurations
Knowledge Check
Manage Envelopes with Authentication or Identity Verification
Objective: After reviewing this topic, you will be able to manage envelopes with recipient authentication and identity verification.
A recipient may fail to authenticate or verify their identity. For example, they may have entered the incorrect code three times when going through access code or phone authentication or their ID may have failed the Docusign ID Verification process.
Envelopes with failed authentication can easily be located from the Agreements tab.
The envelope Status column will display a Delivery Failure.
You can click on the envelope for additional information about managing the failure.
Access Code
SMS / Phone
Knowledge-Based
ID Verification
Congratulations, you have completed this course!
Please provide feedback on this learning experience and content by completing the brief survey below.
Close the Course
EXIT
Lesson 3 - Manage Identity Verification Configurations

Configure eSignature Identity Verification Preferences
Introduction to Identity Verification Preferences
Manage Envelopes with Authentication or Identity Verification
Manage Identity Verification Configurations
Knowledge Check
Manage Identity Verification Configurations
Objective: After reviewing this topic, you will be able to add and customize identity verification configurations.
Click Admin and then Identity Verification to manage the identity verification options available to your users when they send envelopes.
You can view, customize, and activate or deactivate existing configurations.
You can also add a new configuration by selecting from a list of pre-configured identity verifications.
Note: The configuration types with the EU AES and EU QES labels can help you comply with the Advanced Electronic Signature and Qualified Electronic Signature requirements set by the European Union and United Kingdom eIDAS regulations.
Note: The identity verification configuration name and description are not translated. Senders see the text in the language it is written.
Name Variation Level
Accepted IDs
Stored Data from IDs
How to add ID Verification to an account?﻿
Click the button to the right to learn more about adding identity verification configurations.
SUPPORT
Click Edit to edit an existing configuration.
Click the dropdown menu to:
Create a Copy of an existing configuration.
Activate or Deactivate your configuration.
Delete your configuration.
Manage Envelopes with Authentication or Identity Verification
Objective: After reviewing this topic, you will be able to manage envelopes with recipient authentication and identity verification.
A recipient may fail to authenticate or verify their identity. For example, they may have entered the incorrect code three times when going through access code or phone authentication or their ID may have failed the Docusign ID Verification process.
Envelopes with failed authentication can easily be located from the Agreements tab.
The envelope Status column will display a Delivery Failure.
You can click on the envelope for additional information about managing the failure.
Access Code
SMS / Phone
Knowledge-Based
ID Verification
Lesson 4 - Knowledge Check

Configure eSignature Identity Verification Preferences
Introduction to Identity Verification Preferences
Manage Envelopes with Authentication or Identity Verification
Manage Identity Verification Configurations
Knowledge Check
Lesson 2 - Manage Envelopes with Authentication or Identity Verification
Manage Identity Verification Configurations
Objective: After reviewing this topic, you will be able to add and customize identity verification configurations.
Click Admin and then Identity Verification to manage the identity verification options available to your users when they send envelopes.
You can view, customize, and activate or deactivate existing configurations.
You can also add a new configuration by selecting from a list of pre-configured identity verifications.
Note: The configuration types with the EU AES and EU QES labels can help you comply with the Advanced Electronic Signature and Qualified Electronic Signature requirements set by the European Union and United Kingdom eIDAS regulations.
Note: The identity verification configuration name and description are not translated. Senders see the text in the language it is written.
Name Variation Level
Accepted IDs
Stored Data from IDs
How to add ID Verification to an account?﻿
Click the button to the right to learn more about adding identity verification configurations.
SUPPORT
Click Edit to edit an existing configuration.
Click the dropdown menu to:
Create a Copy of an existing configuration.
Activate or Deactivate your configuration.
Delete your configuration.
Lesson 4 - Knowledge Check

Configure eSignature Identity Verification Preferences
Introduction to Identity Verification Preferences
Manage Envelopes with Authentication or Identity Verification
Manage Identity Verification Configurations
Knowledge Check
Manage Envelopes with Authentication or Identity Verification
Objective: After reviewing this topic, you will be able to manage envelopes with recipient authentication and identity verification.
A recipient may fail to authenticate or verify their identity. For example, they may have entered the incorrect code three times when going through access code or phone authentication or their ID may have failed the Docusign ID Verification process.
Envelopes with failed authentication can easily be located from the Agreements tab.
The envelope Status column will display a Delivery Failure.
You can click on the envelope for additional information about managing the failure.
Access Code
SMS / Phone
Knowledge-Based
ID Verification
Manage Identity Verification Configurations
Objective: After reviewing this topic, you will be able to add and customize identity verification configurations.
Click Admin and then Identity Verification to manage the identity verification options available to your users when they send envelopes.
You can view, customize, and activate or deactivate existing configurations.
You can also add a new configuration by selecting from a list of pre-configured identity verifications.
Note: The configuration types with the EU AES and EU QES labels can help you comply with the Advanced Electronic Signature and Qualified Electronic Signature requirements set by the European Union and United Kingdom eIDAS regulations.
Note: The identity verification configuration name and description are not translated. Senders see the text in the language it is written.
Name Variation Level
Accepted IDs
Stored Data from IDs
How to add ID Verification to an account?﻿
Click the button to the right to learn more about adding identity verification configurations.
SUPPORT
Click Edit to edit an existing configuration.
Click the dropdown menu to:
Create a Copy of an existing configuration.
Activate or Deactivate your configuration.
Delete your configuration.
Lesson 3 - Manage Identity Verification Configurations

Configure eSignature Identity Verification Preferences
Introduction to Identity Verification Preferences
Manage Envelopes with Authentication or Identity Verification
Manage Identity Verification Configurations
Knowledge Check
Lesson 1 - Introduction to Identity Verification Preferences
Manage Envelopes with Authentication or Identity Verification
Objective: After reviewing this topic, you will be able to manage envelopes with recipient authentication and identity verification.
A recipient may fail to authenticate or verify their identity. For example, they may have entered the incorrect code three times when going through access code or phone authentication or their ID may have failed the Docusign ID Verification process.
Envelopes with failed authentication can easily be located from the Agreements tab.
The envelope Status column will display a Delivery Failure.
You can click on the envelope for additional information about managing the failure.
Access Code
SMS / Phone
Click the Resend button to generate a new email for the recipient, giving them another opportunity to pass SMS or phone authentication.
You can also click the Correct button to change the phone number used for SMS, phone call, or phone authentication.
Knowledge-Based
ID Verification
Lesson 3 - Manage Identity Verification Configurations

Configure eSignature Identity Verification Preferences
Introduction to Identity Verification Preferences
Manage Envelopes with Authentication or Identity Verification
Manage Identity Verification Configurations
Knowledge Check
Lesson 1 - Introduction to Identity Verification Preferences
Manage Envelopes with Authentication or Identity Verification
Objective: After reviewing this topic, you will be able to manage envelopes with recipient authentication and identity verification.
A recipient may fail to authenticate or verify their identity. For example, they may have entered the incorrect code three times when going through access code or phone authentication or their ID may have failed the Docusign ID Verification process.
Envelopes with failed authentication can easily be located from the Agreements tab.
The envelope Status column will display a Delivery Failure.
You can click on the envelope for additional information about managing the failure.
Access Code
SMS / Phone
Knowledge-Based
Click the Resend button to generate a new email for the recipient, giving them another opportunity to answer the KBA questions.
You can also click the Correct button to change the authentication method.
Note: KBA failures are most often due to the identity verification service being unable to validate the signer's identity.
Signers may be prevented from reattempting KBA within a certain time frame after too many failures. For example, a common configuration locks recipients out for 24 hours if they have failed authentication twice within 24 hours. These rules may vary by account.
KBA is powered by LexisNexis Risk Solutions. If your recipient is having difficulty passing knowledge-based authentication, they can request a Personal Disclosure Report from LexisNexis: https://personalreports.lexisnexis.com/
ID Verification
Lesson 3 - Manage Identity Verification Configurations

Configure eSignature Identity Verification Preferences
Introduction to Identity Verification Preferences
Manage Envelopes with Authentication or Identity Verification
Manage Identity Verification Configurations
Knowledge Check
Lesson 1 - Introduction to Identity Verification Preferences
Manage Envelopes with Authentication or Identity Verification
Objective: After reviewing this topic, you will be able to manage envelopes with recipient authentication and identity verification.
A recipient may fail to authenticate or verify their identity. For example, they may have entered the incorrect code three times when going through access code or phone authentication or their ID may have failed the Docusign ID Verification process.
Envelopes with failed authentication can easily be located from the Agreements tab.
The envelope Status column will display a Delivery Failure.
You can click on the envelope for additional information about managing the failure.
Access Code
SMS / Phone
Knowledge-Based
ID Verification
Depending on whether or not the manual review option is enabled on the account, you may need to:
Click Resend to give another chance to the recipients to pass ID Verification or click Correct and choose another identity verification method.
Manually review the recipient's id document and either Approve or Reject it. If the option is enabled for your account, recipients will need to enter a code received via SMS to access their envelopes once their ID has been approved.
Lesson 3 - Manage Identity Verification Configurations

Configure eSignature Identity Verification Preferences
Introduction to Identity Verification Preferences
Manage Envelopes with Authentication or Identity Verification
Manage Identity Verification Configurations
Knowledge Check
Manage Identity Verification Configurations
Objective: After reviewing this topic, you will be able to add and customize identity verification configurations.
Click Admin and then Identity Verification to manage the identity verification options available to your users when they send envelopes.
You can view, customize, and activate or deactivate existing configurations.
You can also add a new configuration by selecting from a list of pre-configured identity verifications.
Note: The configuration types with the EU AES and EU QES labels can help you comply with the Advanced Electronic Signature and Qualified Electronic Signature requirements set by the European Union and United Kingdom eIDAS regulations.
Note: The identity verification configuration name and description are not translated. Senders see the text in the language it is written.
Name Variation Level
Accepted IDs
Stored Data from IDs
How to add ID Verification to an account?﻿
Click the button to the right to learn more about adding identity verification configurations.
SUPPORT
Click Edit to edit an existing configuration.
Click the dropdown menu to:
Create a Copy of an existing configuration.
Activate or Deactivate your configuration.
Delete your configuration.
Manage Envelopes with Authentication or Identity Verification
Objective: After reviewing this topic, you will be able to manage envelopes with recipient authentication and identity verification.
A recipient may fail to authenticate or verify their identity. For example, they may have entered the incorrect code three times when going through access code or phone authentication or their ID may have failed the Docusign ID Verification process.
Envelopes with failed authentication can easily be located from the Agreements tab.
The envelope Status column will display a Delivery Failure.
You can click on the envelope for additional information about managing the failure.
Access Code
SMS / Phone
Knowledge-Based
ID Verification
Depending on whether or not the manual review option is enabled on the account, you may need to:
Click Resend to give another chance to the recipients to pass ID Verification or click Correct and choose another identity verification method.
Manually review the recipient's id document and either Approve or Reject it. If the option is enabled for your account, recipients will need to enter a code received via SMS to access their envelopes once their ID has been approved.
Lesson 4 - Knowledge Check

Configure eSignature Identity Verification Preferences
Introduction to Identity Verification Preferences
Manage Envelopes with Authentication or Identity Verification
Manage Identity Verification Configurations
Knowledge Check
Which of the following authentication and identity verification methods incur a per-use fee? Select all that apply.
Access code authentication
Knowledge-based authentication
Phone authentication
ID Verification
SUBMIT
Incorrect
Phone authentication, knowledge-based authentication, and ID Verification incur a per use fee.
TAKE AGAIN
Which menu should your users select to add an authentication or identity verification method for a recipient?
Advanced Options
Customize
Recipient Settings
SUBMIT
Incorrect
To add an authentication or identity verification method for a recipient, select the Customize menu, and then select Add access code authentication or Add identity verification.
TAKE AGAIN
You added an access code for a recipient and the recipient forgot their access code. Which action should you take?
Void the existing envelope and send a new envelope with a different code.
Click Resend on the envelope to send a new notification to the recipient.
Contact your administrator and ask them to give you the access code.
Open the envelope to locate the code and provide it to the recipient.
SUBMIT
Incorrect
You can open the envelope to find the access code you selected for the recipient.
TAKE AGAIN
How can a sender access the stored data from the identification process?
Download the envelope documents.
Print the envelope history.
Open the envelope, click More, and View Details.
Open the envelope, click More, and Form Data.
SUBMIT
Incorrect
You can access the stored data from the identification process by opening the envelope, clicking More, and selecting View Details.
TAKE AGAIN
Manage Identity Verification Configurations
Objective: After reviewing this topic, you will be able to add and customize identity verification configurations.
Click Admin and then Identity Verification to manage the identity verification options available to your users when they send envelopes.
You can view, customize, and activate or deactivate existing configurations.
You can also add a new configuration by selecting from a list of pre-configured identity verifications.
Note: The configuration types with the EU AES and EU QES labels can help you comply with the Advanced Electronic Signature and Qualified Electronic Signature requirements set by the European Union and United Kingdom eIDAS regulations.
Note: The identity verification configuration name and description are not translated. Senders see the text in the language it is written.
Name Variation Level
Accepted IDs
Stored Data from IDs
How to add ID Verification to an account?﻿
Click the button to the right to learn more about adding identity verification configurations.
SUPPORT
Click Edit to edit an existing configuration.
Click the dropdown menu to:
Create a Copy of an existing configuration.
Activate or Deactivate your configuration.
Delete your configuration.

## Docusign Extension Apps

### Build Extension Apps for the Docusign App Center 30 min

Build Extension Apps for the Docusign App Center
Introduction to Extension Apps
Register your App: Forms-Based Experience
Register your App: Edit a Manifest File
Test and Publish your Extension App
Lesson 1 - Introduction to Extension Apps
Register your App: Forms-Based Experience
Objective: After reviewing this topic, you will be able to register an extension app via a forms-based experience.
Note: This lesson covers how to register an extension app via the forms-based experience. If you prefer to register your app by editing the JSON manifest file, go directly to the next lesson.
Registering an extension app requires you to define the app properties, including the name, description, publisher information, distribution level, and details required to launch requests to the external API that provides the extension functionality.
You can register your app from the Docusign Developer Console
by using a forms-based experience.
To do so, you must have a Docusign developer account. If you don't already have one, you can create a developer account
on the Docusign Developer Center.
Register your App
Follow these steps to register an extension app by using a forms-based experience:
1
From the Developer Console
, click Create App and select Using a form-based experience.
2
Complete the Tell us about your app form.
App name: Provide a descriptive name for your app which will appear in your app's listing and when selecting it in Docusign Workflow Builder, Docusign Agreement Manager, and Docusign eSignature. Each extension app that you register must have a unique name.
Published by and Support email: Provide your organization name and support email address, which will appear in your app's listing.
Distribution Type: Select Public to allow all App Center users to install your app or select Private to allow only a specific list of accounts to install your app. To learn more, review the Choosing private distribution instead of public
guide.
Extension: Choose at least one type of extension (File Input Output, Data Input Output, Data Verification, or Connected Fields). You will configure the extension later. To learn more about each extension type, review the Supported extensions
guide.
3
Click Create App.
You are taken to the App Overview page where you can test, preview, and publish your app.
Your app is also assigned an App ID that you can provide if you need to reach out to Docusign about your extension app.
Configure your App
Once you have registered your app, you will need to update your integration details and your App Center listing.
Update your Integration Details
Follow the steps below to update your integration details:
1
Click Integration Details in the left panel.
2
Click Edit below Connection to enable your app to obtain authorization from the external API service or identity provider.
Basic Information
Parameters
Custom Config
Auth Params
Extension App Authorization
Select the button to the right to learn more about how to set up the necessary authorization for your extension app.
DEVELOPER CENTER
3
Click Edit below Extensions & Actions to configure your app functionality.
Then, enter or update the extension and action details:
Provide your extension basic information, including the Extension Name and Description.
Provide the actions details, including the Name, Description, and Params URI for each action included in your app.
Click Save when you are finished.
You can also click Add Extension to add another extension to your app. You will need to select an extension category and update your extension and action settings.
Integration Details
Select the link to the right to learn more about updating your integration details.
DEVELOPER CENTER
Update your App Center Listing
Click App Center Listing to configure the text and images that will appear on the Docusign App Center and to control your app distribution.
This includes:
Uploading screenshots and an icon for your app.
Updating your basic app information, publisher details, and contact information.
Configuring your app distribution details (public or private and regions where your app is available).
App Center Listing
Select the link to the right to learn more about updating your App Center listing.
DEVELOPER CENTER
Lesson 3 - Register your App: Edit a Manifest File

Build Extension Apps for the Docusign App Center
RESUME COURSE
Welcome to the Build Extension Apps for the Docusign App Center self-paced course. After reviewing this course, you will be able to:
Describe the benefits of developing and using extension applications.
Register an extension app using a forms-based experience.
Register an extension app by editing a JSON manifest file.
Test and publish your extension app.
Introduction to Extension Apps
Register your App: Forms-Based Experience
Register your App: Edit a Manifest File
Test and Publish your Extension App

Build Extension Apps for the Docusign App Center
Introduction to Extension Apps
Register your App: Forms-Based Experience
Register your App: Edit a Manifest File
Test and Publish your Extension App
Register your App: Forms-Based Experience
Objective: After reviewing this topic, you will be able to register an extension app via a forms-based experience.
Note: This lesson covers how to register an extension app via the forms-based experience. If you prefer to register your app by editing the JSON manifest file, go directly to the next lesson.
Registering an extension app requires you to define the app properties, including the name, description, publisher information, distribution level, and details required to launch requests to the external API that provides the extension functionality.
You can register your app from the Docusign Developer Console
by using a forms-based experience.
To do so, you must have a Docusign developer account. If you don't already have one, you can create a developer account
on the Docusign Developer Center.
Register your App
Follow these steps to register an extension app by using a forms-based experience:
1
From the Developer Console
, click Create App and select Using a form-based experience.
2
Complete the Tell us about your app form.
App name: Provide a descriptive name for your app which will appear in your app's listing and when selecting it in Docusign Workflow Builder, Docusign Agreement Manager, and Docusign eSignature. Each extension app that you register must have a unique name.
Published by and Support email: Provide your organization name and support email address, which will appear in your app's listing.
Distribution Type: Select Public to allow all App Center users to install your app or select Private to allow only a specific list of accounts to install your app. To learn more, review the Choosing private distribution instead of public
guide.
Extension: Choose at least one type of extension (File Input Output, Data Input Output, Data Verification, or Connected Fields). You will configure the extension later. To learn more about each extension type, review the Supported extensions
guide.
3
Click Create App.
You are taken to the App Overview page where you can test, preview, and publish your app.
Your app is also assigned an App ID that you can provide if you need to reach out to Docusign about your extension app.
Configure your App
Once you have registered your app, you will need to update your integration details and your App Center listing.
Update your Integration Details
Follow the steps below to update your integration details:
1
Click Integration Details in the left panel.
2
Click Edit below Connection to enable your app to obtain authorization from the external API service or identity provider.
Basic Information
Parameters
Custom Config
Auth Params
Extension App Authorization
Select the button to the right to learn more about how to set up the necessary authorization for your extension app.
DEVELOPER CENTER
3
Click Edit below Extensions & Actions to configure your app functionality.
Then, enter or update the extension and action details:
Provide your extension basic information, including the Extension Name and Description.
Provide the actions details, including the Name, Description, and Params URI for each action included in your app.
Click Save when you are finished.
You can also click Add Extension to add another extension to your app. You will need to select an extension category and update your extension and action settings.
Integration Details
Select the link to the right to learn more about updating your integration details.
DEVELOPER CENTER
Update your App Center Listing
Click App Center Listing to configure the text and images that will appear on the Docusign App Center and to control your app distribution.
This includes:
Uploading screenshots and an icon for your app.
Updating your basic app information, publisher details, and contact information.
Configuring your app distribution details (public or private and regions where your app is available).
App Center Listing
Select the link to the right to learn more about updating your App Center listing.
DEVELOPER CENTER
Congratulations, you have completed this course!
Please provide feedback on this learning experience and content by completing the brief survey below.
Close the Course
EXIT
Lesson 3 - Register your App: Edit a Manifest File

Build Extension Apps for the Docusign App Center
Introduction to Extension Apps
Register your App: Forms-Based Experience
Register your App: Edit a Manifest File
Test and Publish your Extension App
Register your App: Edit a Manifest File
Objective: After reviewing this topic, you will be able to register an extension app by editing a manifest file.
Note: This lesson covers how to register an extension app by editing a JSON manifest file. Registering an app via the forms-based experience is covered in the previous lesson in this course.
An extension app manifest file defines the extension app properties, including the name, description, publisher information, distribution level, and details required to launch requests to the external API that provides the extension functionality.
You can register your app from the Docusign Developer Console
by editing a JSON manifest file.
To do so, you must have a Docusign developer account. If you don't already have one, you can create a developer account
on the Docusign Developer Center.
Build your Extension App Manifest File
Follow these steps to build an extension app manifest file and upload it to the Developer Console:
1
From the Developer Console
, click Create App and select By editing the manifest.
2
Use the built-in editor, or click the Download icon to edit the template locally.
Best Practice
We recommend using the built-in app editor to make changes to your manifest file as the editor offers real-time automatic validation for common issues. It will save you a lot of time going back and forth from your other JSON editor when you need to make updates.
3
Edit the manifest file with your app details.
APP DETAILS
CONNECTIONS
EXTENSIONS
ACTIONS
Specify your app details in the first part of the file as shown in the JSON snippet below. These details will appear in the Docusign App Center when the extension app is published.
name: Provide a descriptive name for your app. Each extension app that you register needs to have a unique name.
publicationRegions: (public apps only) Choose from which regions your app can be installed. To learn more, review the Globalization
guide.
distribution: Enter PUBLIC to allow all App Center users to install your app or enter PRIVATE to allow only a specific list of accounts to install your app. To learn more, review the Choosing private distribution instead of public
guide.
description: Provide a short and long description.
publisher: Provide your organization name, email, phone number, and website.
termsOfServiceUrl: Provide the URLs of your terms of service, privacy policy, and support.
icon and screenshots: To add an icon and screenshots to your extension app, set the values of icon.data or screenshots[].data to the base64 representation of your images. You can add up to four screenshots.
Review the Extension app best practices
for more information.
Notes:
Review the App Manifest Reference
for the full list of supported elements.
If your app will use external service endpoints that don’t conform to the Docusign Action
schema, you may need to set up an API proxy
to translate the external API’s requests and responses to the format that Docusign expects.
You will need to obtain the external service, identity provider, and API proxy information that you will need to configure your extension app. This includes endpoint URLs, authorization
details, and required parameters in requests to the endpoints and in the responses.
Once you have set all of those values, upload your extension app manifest file on the Developer Console.
4
Click Select File and upload your JSON manifest file or paste the file content in the built-in editor.
5
Click Validate to verify that your file contains no errors.
Best Practice
You can find a list of possible errors with details on how to troubleshoot them on the Troubleshooting manifest errors
guide.
6
Once your manifest has passed all validation checks, click Create App to finish registering your application.
You are taken to the App Overview page where you can test, preview, and publish your app.
Your app is also assigned an App ID that you can provide if you need to reach out to Docusign about your extension app.
Register your App: Forms-Based Experience
Objective: After reviewing this topic, you will be able to register an extension app via a forms-based experience.
Note: This lesson covers how to register an extension app via the forms-based experience. If you prefer to register your app by editing the JSON manifest file, go directly to the next lesson.
Registering an extension app requires you to define the app properties, including the name, description, publisher information, distribution level, and details required to launch requests to the external API that provides the extension functionality.
You can register your app from the Docusign Developer Console
by using a forms-based experience.
To do so, you must have a Docusign developer account. If you don't already have one, you can create a developer account
on the Docusign Developer Center.
Register your App
Follow these steps to register an extension app by using a forms-based experience:
1
From the Developer Console
, click Create App and select Using a form-based experience.
2
Complete the Tell us about your app form.
App name: Provide a descriptive name for your app which will appear in your app's listing and when selecting it in Docusign Workflow Builder, Docusign Agreement Manager, and Docusign eSignature. Each extension app that you register must have a unique name.
Published by and Support email: Provide your organization name and support email address, which will appear in your app's listing.
Distribution Type: Select Public to allow all App Center users to install your app or select Private to allow only a specific list of accounts to install your app. To learn more, review the Choosing private distribution instead of public
guide.
Extension: Choose at least one type of extension (File Input Output, Data Input Output, Data Verification, or Connected Fields). You will configure the extension later. To learn more about each extension type, review the Supported extensions
guide.
3
Click Create App.
You are taken to the App Overview page where you can test, preview, and publish your app.
Your app is also assigned an App ID that you can provide if you need to reach out to Docusign about your extension app.
Configure your App
Once you have registered your app, you will need to update your integration details and your App Center listing.
Update your Integration Details
Follow the steps below to update your integration details:
1
Click Integration Details in the left panel.
2
Click Edit below Connection to enable your app to obtain authorization from the external API service or identity provider.
Basic Information
Parameters
Custom Config
Auth Params
Extension App Authorization
Select the button to the right to learn more about how to set up the necessary authorization for your extension app.
DEVELOPER CENTER
3
Click Edit below Extensions & Actions to configure your app functionality.
Then, enter or update the extension and action details:
Provide your extension basic information, including the Extension Name and Description.
Provide the actions details, including the Name, Description, and Params URI for each action included in your app.
Click Save when you are finished.
You can also click Add Extension to add another extension to your app. You will need to select an extension category and update your extension and action settings.
Integration Details
Select the link to the right to learn more about updating your integration details.
DEVELOPER CENTER
Update your App Center Listing
Click App Center Listing to configure the text and images that will appear on the Docusign App Center and to control your app distribution.
This includes:
Uploading screenshots and an icon for your app.
Updating your basic app information, publisher details, and contact information.
Configuring your app distribution details (public or private and regions where your app is available).
App Center Listing
Select the link to the right to learn more about updating your App Center listing.
DEVELOPER CENTER
Lesson 4 - Test and Publish your Extension App

Build Extension Apps for the Docusign App Center
Introduction to Extension Apps
Register your App: Forms-Based Experience
Register your App: Edit a Manifest File
Test and Publish your Extension App
Objective: After reviewing this topic, you will be able to test and publish your extension app.
Once you have registered your app, you will need to test your extension app to make sure it works as expected.
Click App Testing in the left panel to test your application.
Test your Application
The App Testing page displays.
Once you have completed all the tests and confirmed your app is functioning correctly, review the extension app publishing guidelines
to ensure it meets the extension app requirements and best practices.
Note: You will need to send your app for review to publish it on the Docusign App Center as detailed below.
Publish your Application
Click Publish to App Center and then Submit to submit your app for review and publish it to the Docusign App Center.
Your application will go through a review process that evaluates the business, technical, security, and functional aspects of your extension app.
Once you’ve submitted your extension app for review, you can check the status of the review in the Developer Console or cancel an in-progress review. You’ll be notified of any issues that Docusign finds, receive guidance on how to correct them, and be able to resubmit the extension app for review after making the updates.
After a successful review, your extension app will appear in Approved status in the Developer Console. You can then click Publish to App Center to make it available on the App Center.
•
If you set your app distribution to PUBLIC, you will need to click a button to make your app available in the App Center for all customers.
•
If you set your app distribution to PRIVATE, you will need to select the production Docusign accounts allowed to install your app.
Share your Private App
Click Add and provide the production account(s) ID (also called GUID) for the account(s) you wish to share your app with. Administrators of each selected account will be able to install the app. Select the tab below to learn how to locate an account ID.
Provide an Alias for the account(s) to help you identify the account(s) and select the checkmark to save your changes.
How to Locate an Account ID (GUID)
The Status will be set to Pending until the administrator for the selected account accepts the extension app in the App Center.
The Status will be updated to Accepted once they have added the app to their account.
You can click the delete icon if you need to remove the app from a customer's account.
Note: The account administrator is not notified when you remove an app. You should be careful removing an app after it has already been accepted, as it may be in use by customers.
Manage Extension Apps
You can view and manage your extension apps from the Developer Console home page.
You can view your application's details including the name, distribution level (public or private), status (Draft, In Review, Approved, Rejected, Live, and Discontinued), and the last updated date.
Click the three vertical dots to return to the App Overview page, edit or download your manifest file, or delete your app.
Register your App: Edit a Manifest File
Objective: After reviewing this topic, you will be able to register an extension app by editing a manifest file.
Note: This lesson covers how to register an extension app by editing a JSON manifest file. Registering an app via the forms-based experience is covered in the previous lesson in this course.
An extension app manifest file defines the extension app properties, including the name, description, publisher information, distribution level, and details required to launch requests to the external API that provides the extension functionality.
You can register your app from the Docusign Developer Console
by editing a JSON manifest file.
To do so, you must have a Docusign developer account. If you don't already have one, you can create a developer account
on the Docusign Developer Center.
Build your Extension App Manifest File
Follow these steps to build an extension app manifest file and upload it to the Developer Console:
1
From the Developer Console
, click Create App and select By editing the manifest.
2
Use the built-in editor, or click the Download icon to edit the template locally.
Best Practice
We recommend using the built-in app editor to make changes to your manifest file as the editor offers real-time automatic validation for common issues. It will save you a lot of time going back and forth from your other JSON editor when you need to make updates.
3
Edit the manifest file with your app details.
APP DETAILS
CONNECTIONS
EXTENSIONS
ACTIONS
Specify your app details in the first part of the file as shown in the JSON snippet below. These details will appear in the Docusign App Center when the extension app is published.
name: Provide a descriptive name for your app. Each extension app that you register needs to have a unique name.
publicationRegions: (public apps only) Choose from which regions your app can be installed. To learn more, review the Globalization
guide.
distribution: Enter PUBLIC to allow all App Center users to install your app or enter PRIVATE to allow only a specific list of accounts to install your app. To learn more, review the Choosing private distribution instead of public
guide.
description: Provide a short and long description.
publisher: Provide your organization name, email, phone number, and website.
termsOfServiceUrl: Provide the URLs of your terms of service, privacy policy, and support.
icon and screenshots: To add an icon and screenshots to your extension app, set the values of icon.data or screenshots[].data to the base64 representation of your images. You can add up to four screenshots.
Review the Extension app best practices
for more information.
Notes:
Review the App Manifest Reference
for the full list of supported elements.
If your app will use external service endpoints that don’t conform to the Docusign Action
schema, you may need to set up an API proxy
to translate the external API’s requests and responses to the format that Docusign expects.
You will need to obtain the external service, identity provider, and API proxy information that you will need to configure your extension app. This includes endpoint URLs, authorization
details, and required parameters in requests to the endpoints and in the responses.
Once you have set all of those values, upload your extension app manifest file on the Developer Console.
4
Click Select File and upload your JSON manifest file or paste the file content in the built-in editor.
5
Click Validate to verify that your file contains no errors.
Best Practice
You can find a list of possible errors with details on how to troubleshoot them on the Troubleshooting manifest errors
guide.
6
Once your manifest has passed all validation checks, click Create App to finish registering your application.
You are taken to the App Overview page where you can test, preview, and publish your app.
Your app is also assigned an App ID that you can provide if you need to reach out to Docusign about your extension app.

Build Extension Apps for the Docusign App Center
Introduction to Extension Apps
Register your App: Forms-Based Experience
Register your App: Edit a Manifest File
Test and Publish your Extension App
Lesson 3 - Register your App: Edit a Manifest File
Test and Publish your Extension App
Objective: After reviewing this topic, you will be able to test and publish your extension app.
Once you have registered your app, you will need to test your extension app to make sure it works as expected.
Click App Testing in the left panel to test your application.
Test your Application
The App Testing page displays.
Once you have completed all the tests and confirmed your app is functioning correctly, review the extension app publishing guidelines
to ensure it meets the extension app requirements and best practices.
Note: You will need to send your app for review to publish it on the Docusign App Center as detailed below.
Publish your Application
Click Publish to App Center and then Submit to submit your app for review and publish it to the Docusign App Center.
Your application will go through a review process that evaluates the business, technical, security, and functional aspects of your extension app.
Once you’ve submitted your extension app for review, you can check the status of the review in the Developer Console or cancel an in-progress review. You’ll be notified of any issues that Docusign finds, receive guidance on how to correct them, and be able to resubmit the extension app for review after making the updates.
After a successful review, your extension app will appear in Approved status in the Developer Console. You can then click Publish to App Center to make it available on the App Center.
•
If you set your app distribution to PUBLIC, you will need to click a button to make your app available in the App Center for all customers.
•
If you set your app distribution to PRIVATE, you will need to select the production Docusign accounts allowed to install your app.
Share your Private App
Click Add and provide the production account(s) ID (also called GUID) for the account(s) you wish to share your app with. Administrators of each selected account will be able to install the app. Select the tab below to learn how to locate an account ID.
Provide an Alias for the account(s) to help you identify the account(s) and select the checkmark to save your changes.
How to Locate an Account ID (GUID)
The Status will be set to Pending until the administrator for the selected account accepts the extension app in the App Center.
The Status will be updated to Accepted once they have added the app to their account.
You can click the delete icon if you need to remove the app from a customer's account.
Note: The account administrator is not notified when you remove an app. You should be careful removing an app after it has already been accepted, as it may be in use by customers.
Manage Extension Apps
You can view and manage your extension apps from the Developer Console home page.
You can view your application's details including the name, distribution level (public or private), status (Draft, In Review, Approved, Rejected, Live, and Discontinued), and the last updated date.
Click the three vertical dots to return to the App Overview page, edit or download your manifest file, or delete your app.

Build Extension Apps for the Docusign App Center
Introduction to Extension Apps
Register your App: Forms-Based Experience
Register your App: Edit a Manifest File
Test and Publish your Extension App
Register your App: Edit a Manifest File
Objective: After reviewing this topic, you will be able to register an extension app by editing a manifest file.
Note: This lesson covers how to register an extension app by editing a JSON manifest file. Registering an app via the forms-based experience is covered in the previous lesson in this course.
An extension app manifest file defines the extension app properties, including the name, description, publisher information, distribution level, and details required to launch requests to the external API that provides the extension functionality.
You can register your app from the Docusign Developer Console
by editing a JSON manifest file.
To do so, you must have a Docusign developer account. If you don't already have one, you can create a developer account
on the Docusign Developer Center.
Build your Extension App Manifest File
Follow these steps to build an extension app manifest file and upload it to the Developer Console:
1
From the Developer Console
, click Create App and select By editing the manifest.
2
Use the built-in editor, or click the Download icon to edit the template locally.
Best Practice
We recommend using the built-in app editor to make changes to your manifest file as the editor offers real-time automatic validation for common issues. It will save you a lot of time going back and forth from your other JSON editor when you need to make updates.
3
Edit the manifest file with your app details.
APP DETAILS
CONNECTIONS
EXTENSIONS
ACTIONS
Specify your app details in the first part of the file as shown in the JSON snippet below. These details will appear in the Docusign App Center when the extension app is published.
name: Provide a descriptive name for your app. Each extension app that you register needs to have a unique name.
publicationRegions: (public apps only) Choose from which regions your app can be installed. To learn more, review the Globalization
guide.
distribution: Enter PUBLIC to allow all App Center users to install your app or enter PRIVATE to allow only a specific list of accounts to install your app. To learn more, review the Choosing private distribution instead of public
guide.
description: Provide a short and long description.
publisher: Provide your organization name, email, phone number, and website.
termsOfServiceUrl: Provide the URLs of your terms of service, privacy policy, and support.
icon and screenshots: To add an icon and screenshots to your extension app, set the values of icon.data or screenshots[].data to the base64 representation of your images. You can add up to four screenshots.
Review the Extension app best practices
for more information.
Notes:
Review the App Manifest Reference
for the full list of supported elements.
If your app will use external service endpoints that don’t conform to the Docusign Action
schema, you may need to set up an API proxy
to translate the external API’s requests and responses to the format that Docusign expects.
You will need to obtain the external service, identity provider, and API proxy information that you will need to configure your extension app. This includes endpoint URLs, authorization
details, and required parameters in requests to the endpoints and in the responses.
Once you have set all of those values, upload your extension app manifest file on the Developer Console.
4
Click Select File and upload your JSON manifest file or paste the file content in the built-in editor.
5
Click Validate to verify that your file contains no errors.
Best Practice
You can find a list of possible errors with details on how to troubleshoot them on the Troubleshooting manifest errors
guide.
6
Once your manifest has passed all validation checks, click Create App to finish registering your application.
You are taken to the App Overview page where you can test, preview, and publish your app.
Your app is also assigned an App ID that you can provide if you need to reach out to Docusign about your extension app.
Test and Publish your Extension App
Objective: After reviewing this topic, you will be able to test and publish your extension app.
Once you have registered your app, you will need to test your extension app to make sure it works as expected.
Click App Testing in the left panel to test your application.
Test your Application
The App Testing page displays.
Once you have completed all the tests and confirmed your app is functioning correctly, review the extension app publishing guidelines
to ensure it meets the extension app requirements and best practices.
Note: You will need to send your app for review to publish it on the Docusign App Center as detailed below.
Publish your Application
Click Publish to App Center and then Submit to submit your app for review and publish it to the Docusign App Center.
Your application will go through a review process that evaluates the business, technical, security, and functional aspects of your extension app.
Once you’ve submitted your extension app for review, you can check the status of the review in the Developer Console or cancel an in-progress review. You’ll be notified of any issues that Docusign finds, receive guidance on how to correct them, and be able to resubmit the extension app for review after making the updates.
After a successful review, your extension app will appear in Approved status in the Developer Console. You can then click Publish to App Center to make it available on the App Center.
•
If you set your app distribution to PUBLIC, you will need to click a button to make your app available in the App Center for all customers.
•
If you set your app distribution to PRIVATE, you will need to select the production Docusign accounts allowed to install your app.
Share your Private App
Click Add and provide the production account(s) ID (also called GUID) for the account(s) you wish to share your app with. Administrators of each selected account will be able to install the app. Select the tab below to learn how to locate an account ID.
Provide an Alias for the account(s) to help you identify the account(s) and select the checkmark to save your changes.
How to Locate an Account ID (GUID)
The Status will be set to Pending until the administrator for the selected account accepts the extension app in the App Center.
The Status will be updated to Accepted once they have added the app to their account.
You can click the delete icon if you need to remove the app from a customer's account.
Note: The account administrator is not notified when you remove an app. You should be careful removing an app after it has already been accepted, as it may be in use by customers.
Manage Extension Apps
You can view and manage your extension apps from the Developer Console home page.
You can view your application's details including the name, distribution level (public or private), status (Draft, In Review, Approved, Rejected, Live, and Discontinued), and the last updated date.
Click the three vertical dots to return to the App Overview page, edit or download your manifest file, or delete your app.
Lesson 4 - Test and Publish your Extension App

Build Extension Apps for the Docusign App Center
Introduction to Extension Apps
Register your App: Forms-Based Experience
Register your App: Edit a Manifest File
Test and Publish your Extension App
Lesson 2 - Register your App: Forms-Based Experience
Register your App: Edit a Manifest File
Objective: After reviewing this topic, you will be able to register an extension app by editing a manifest file.
Note: This lesson covers how to register an extension app by editing a JSON manifest file. Registering an app via the forms-based experience is covered in the previous lesson in this course.
An extension app manifest file defines the extension app properties, including the name, description, publisher information, distribution level, and details required to launch requests to the external API that provides the extension functionality.
You can register your app from the Docusign Developer Console
by editing a JSON manifest file.
To do so, you must have a Docusign developer account. If you don't already have one, you can create a developer account
on the Docusign Developer Center.
Build your Extension App Manifest File
Follow these steps to build an extension app manifest file and upload it to the Developer Console:
1
From the Developer Console
, click Create App and select By editing the manifest.
2
Use the built-in editor, or click the Download icon to edit the template locally.
Best Practice
We recommend using the built-in app editor to make changes to your manifest file as the editor offers real-time automatic validation for common issues. It will save you a lot of time going back and forth from your other JSON editor when you need to make updates.
3
Edit the manifest file with your app details.
APP DETAILS
CONNECTIONS
EXTENSIONS
ACTIONS
Specify your app details in the first part of the file as shown in the JSON snippet below. These details will appear in the Docusign App Center when the extension app is published.
name: Provide a descriptive name for your app. Each extension app that you register needs to have a unique name.
publicationRegions: (public apps only) Choose from which regions your app can be installed. To learn more, review the Globalization
guide.
distribution: Enter PUBLIC to allow all App Center users to install your app or enter PRIVATE to allow only a specific list of accounts to install your app. To learn more, review the Choosing private distribution instead of public
guide.
description: Provide a short and long description.
publisher: Provide your organization name, email, phone number, and website.
termsOfServiceUrl: Provide the URLs of your terms of service, privacy policy, and support.
icon and screenshots: To add an icon and screenshots to your extension app, set the values of icon.data or screenshots[].data to the base64 representation of your images. You can add up to four screenshots.
Review the Extension app best practices
for more information.
Notes:
Review the App Manifest Reference
for the full list of supported elements.
If your app will use external service endpoints that don’t conform to the Docusign Action
schema, you may need to set up an API proxy
to translate the external API’s requests and responses to the format that Docusign expects.
You will need to obtain the external service, identity provider, and API proxy information that you will need to configure your extension app. This includes endpoint URLs, authorization
details, and required parameters in requests to the endpoints and in the responses.
Once you have set all of those values, upload your extension app manifest file on the Developer Console.
4
Click Select File and upload your JSON manifest file or paste the file content in the built-in editor.
5
Click Validate to verify that your file contains no errors.
Best Practice
You can find a list of possible errors with details on how to troubleshoot them on the Troubleshooting manifest errors
guide.
6
Once your manifest has passed all validation checks, click Create App to finish registering your application.
You are taken to the App Overview page where you can test, preview, and publish your app.
Your app is also assigned an App ID that you can provide if you need to reach out to Docusign about your extension app.
Lesson 4 - Test and Publish your Extension App

Build Extension Apps for the Docusign App Center
Introduction to Extension Apps
Register your App: Forms-Based Experience
Register your App: Edit a Manifest File
Test and Publish your Extension App
Lesson 2 - Register your App: Forms-Based Experience
Register your App: Edit a Manifest File
Objective: After reviewing this topic, you will be able to register an extension app by editing a manifest file.
Note: This lesson covers how to register an extension app by editing a JSON manifest file. Registering an app via the forms-based experience is covered in the previous lesson in this course.
An extension app manifest file defines the extension app properties, including the name, description, publisher information, distribution level, and details required to launch requests to the external API that provides the extension functionality.
You can register your app from the Docusign Developer Console
by editing a JSON manifest file.
To do so, you must have a Docusign developer account. If you don't already have one, you can create a developer account
on the Docusign Developer Center.
Build your Extension App Manifest File
Follow these steps to build an extension app manifest file and upload it to the Developer Console:
1
From the Developer Console
, click Create App and select By editing the manifest.
2
Use the built-in editor, or click the Download icon to edit the template locally.
Best Practice
We recommend using the built-in app editor to make changes to your manifest file as the editor offers real-time automatic validation for common issues. It will save you a lot of time going back and forth from your other JSON editor when you need to make updates.
3
Edit the manifest file with your app details.
APP DETAILS
CONNECTIONS
EXTENSIONS
ACTIONS
Specify your extension app’s connections in the next section of the file as shown in the JSON snippet below.
A connections object contains all of the data needed to connect with an external API, API proxy, or identity provider. The connection name must be a unique value that will be used again later when defining the extension app’s actions. To extend your workflow to multiple external platforms, you can register and apply multiple extension apps, one for each platform.
Within the connections object, set these values within the params property:
clientId and clientSecret: These values should come from the external platform or identity provider.
provider: This value should be set to CUSTOM.
scopes: List any scopes that need to be requested during authorization.
customConfig: This object will store the following properties related to your extension app’s custom configuration:
tokenUrl and authorizationUrl: Set these values to the endpoints required to get the access token and authorization.
authorizationParams: Use this property to store any query parameters needed for the authorization endpoint.
authorizationMethod: Set this value to either header or body.
scopeSeparator: Set this value to the delimiter that will be used to separate your needed scopes.
To learn more, review the Connections
guide.
Notes:
Review the App Manifest Reference
for the full list of supported elements.
If your app will use external service endpoints that don’t conform to the Docusign Action
schema, you may need to set up an API proxy
to translate the external API’s requests and responses to the format that Docusign expects.
You will need to obtain the external service, identity provider, and API proxy information that you will need to configure your extension app. This includes endpoint URLs, authorization
details, and required parameters in requests to the endpoints and in the responses.
Once you have set all of those values, upload your extension app manifest file on the Developer Console.
4
Click Select File and upload your JSON manifest file or paste the file content in the built-in editor.
5
Click Validate to verify that your file contains no errors.
Best Practice
You can find a list of possible errors with details on how to troubleshoot them on the Troubleshooting manifest errors
guide.
6
Once your manifest has passed all validation checks, click Create App to finish registering your application.
You are taken to the App Overview page where you can test, preview, and publish your app.
Your app is also assigned an App ID that you can provide if you need to reach out to Docusign about your extension app.
Lesson 4 - Test and Publish your Extension App

Build Extension Apps for the Docusign App Center
Introduction to Extension Apps
Register your App: Forms-Based Experience
Register your App: Edit a Manifest File
Test and Publish your Extension App
Lesson 2 - Register your App: Forms-Based Experience
Register your App: Edit a Manifest File
Objective: After reviewing this topic, you will be able to register an extension app by editing a manifest file.
Note: This lesson covers how to register an extension app by editing a JSON manifest file. Registering an app via the forms-based experience is covered in the previous lesson in this course.
An extension app manifest file defines the extension app properties, including the name, description, publisher information, distribution level, and details required to launch requests to the external API that provides the extension functionality.
You can register your app from the Docusign Developer Console
by editing a JSON manifest file.
To do so, you must have a Docusign developer account. If you don't already have one, you can create a developer account
on the Docusign Developer Center.
Build your Extension App Manifest File
Follow these steps to build an extension app manifest file and upload it to the Developer Console:
1
From the Developer Console
, click Create App and select By editing the manifest.
2
Use the built-in editor, or click the Download icon to edit the template locally.
Best Practice
We recommend using the built-in app editor to make changes to your manifest file as the editor offers real-time automatic validation for common issues. It will save you a lot of time going back and forth from your other JSON editor when you need to make updates.
3
Edit the manifest file with your app details.
APP DETAILS
CONNECTIONS
EXTENSIONS
ACTIONS
Create an extensions object to define the group of tasks that your extension app should execute such as archiving documents or validating data. Create an actions object to define each one of those tasks as shown in the JSON snippet below.
In the extensions object, define the following properties:
template: This value should be set to the unique string identifier that references the predefined extension contract reference for your extension provided by Docusign.
actionReferences: List the actions that make up your extension. The names listed here should match the names of actions defined in the actions object of your extension app manifest.
To learn more, review the Extensions and extension points
guide.
Notes:
Review the App Manifest Reference
for the full list of supported elements.
If your app will use external service endpoints that don’t conform to the Docusign Action
schema, you may need to set up an API proxy
to translate the external API’s requests and responses to the format that Docusign expects.
You will need to obtain the external service, identity provider, and API proxy information that you will need to configure your extension app. This includes endpoint URLs, authorization
details, and required parameters in requests to the endpoints and in the responses.
Once you have set all of those values, upload your extension app manifest file on the Developer Console.
4
Click Select File and upload your JSON manifest file or paste the file content in the built-in editor.
5
Click Validate to verify that your file contains no errors.
Best Practice
You can find a list of possible errors with details on how to troubleshoot them on the Troubleshooting manifest errors
guide.
6
Once your manifest has passed all validation checks, click Create App to finish registering your application.
You are taken to the App Overview page where you can test, preview, and publish your app.
Your app is also assigned an App ID that you can provide if you need to reach out to Docusign about your extension app.
Lesson 4 - Test and Publish your Extension App

Build Extension Apps for the Docusign App Center
Introduction to Extension Apps
Register your App: Forms-Based Experience
Register your App: Edit a Manifest File
Test and Publish your Extension App
Lesson 2 - Register your App: Forms-Based Experience
Register your App: Edit a Manifest File
Objective: After reviewing this topic, you will be able to register an extension app by editing a manifest file.
Note: This lesson covers how to register an extension app by editing a JSON manifest file. Registering an app via the forms-based experience is covered in the previous lesson in this course.
An extension app manifest file defines the extension app properties, including the name, description, publisher information, distribution level, and details required to launch requests to the external API that provides the extension functionality.
You can register your app from the Docusign Developer Console
by editing a JSON manifest file.
To do so, you must have a Docusign developer account. If you don't already have one, you can create a developer account
on the Docusign Developer Center.
Build your Extension App Manifest File
Follow these steps to build an extension app manifest file and upload it to the Developer Console:
1
From the Developer Console
, click Create App and select By editing the manifest.
2
Use the built-in editor, or click the Download icon to edit the template locally.
Best Practice
We recommend using the built-in app editor to make changes to your manifest file as the editor offers real-time automatic validation for common issues. It will save you a lot of time going back and forth from your other JSON editor when you need to make updates.
3
Edit the manifest file with your app details.
APP DETAILS
CONNECTIONS
EXTENSIONS
ACTIONS
Create an actions object to define each task specified in your extensions object, as shown in the JSON snippet below.
Actions are the individual functions that do the work in your extension app. They specify the external platform endpoints to call from your Docusign workflows.
name and description: Provide a name and description for the action. The name value will be referenced in the actionReferences field in the extensions object.
template: This value defines the action contract reference of the action and should be set to the unique string identifier of the template for the contract.
connectionsReference: This value should match the value of the name parameter in the connections object in your extension app manifest.
params: Use this parameter to specify the external API endpoint or API proxy endpoint that will be called by the action.
To learn more, review the Actions
guide.
Notes:
Review the App Manifest Reference
for the full list of supported elements.
If your app will use external service endpoints that don’t conform to the Docusign Action
schema, you may need to set up an API proxy
to translate the external API’s requests and responses to the format that Docusign expects.
You will need to obtain the external service, identity provider, and API proxy information that you will need to configure your extension app. This includes endpoint URLs, authorization
details, and required parameters in requests to the endpoints and in the responses.
Once you have set all of those values, upload your extension app manifest file on the Developer Console.
4
Click Select File and upload your JSON manifest file or paste the file content in the built-in editor.
5
Click Validate to verify that your file contains no errors.
Best Practice
You can find a list of possible errors with details on how to troubleshoot them on the Troubleshooting manifest errors
guide.
6
Once your manifest has passed all validation checks, click Create App to finish registering your application.
You are taken to the App Overview page where you can test, preview, and publish your app.
Your app is also assigned an App ID that you can provide if you need to reach out to Docusign about your extension app.
Lesson 4 - Test and Publish your Extension App



## Exam Gap Topics (official objectives the courses cover lightly)

Sources: Docusign Developer Center pages listed as "Support Resources" in the official Prep Guide.

### Section 1 - Obtain and revoke consent
- Three ways to get consent: **individual consent**, **admin consent for internal apps** (the integration key is owned by your org; granted in Docusign Admin > Connected Apps > Authorize Application), and **admin consent for external apps** (an ISV app; browser goes to `/oauth/auth?response_type=code&scope=openid&client_id=...&redirect_uri=...&admin_consent_scope=signature%20impersonation`).
- Admin consent requires **Access Management** and a **claimed domain**. It applies to users in the reserved domains.
- With `openid`, the response includes an **ID token**. Its `coid` claim lists the consenting organization IDs. This is the only way to get that list. The ID token is not used to call APIs.
- Best practice for JWT/ISV apps: try admin consent, and **always build an individual consent fallback**.
- **Revoking consent**:
  - Individual: Manage Profile > **Connected Apps** > Revoke.
  - Admin-granted consent: revoke in **Docusign Admin**. Users in reserved domains **cannot** revoke individually.
  - Revoking **invalidates refresh tokens** and blocks new tokens. **Live access tokens (including JWT ones) keep working until they expire.**
- `extended` scope = reusable refresh token, **Authorization Code Grant only**. JWT never returns a refresh token (its token lasts 1 hour; mint a new JWT).

### Section 2 - API limits and efficiency score
- Default **3,000 calls/hour per account**, shared by all integrations; resets on the hour. Exceeding it blocks calls until the next hour ("The maximum number of hourly API invocations has been exceeded").
- **Burst limit**: 500 calls per 30 seconds in production, 200 in demo.
- **Polling**: at most **once per 15 minutes per envelope**. Violations can fail Go-Live review. Prefer **Connect**. For catch-up, use `Envelopes:listStatusChanges` with overlapping time spans.
- Per-envelope error codes: `Hourly_Envelope_Polling_Limit_Exceeded`, `Burst_Envelope_Polling_Limit_Exceeded`, `Hourly_APIInvocation_Envelope_Limit_Exceeded`, `Burst_APIInvocation_Envelope_Limit_Exceeded`.
- Read the `X-RateLimit-*` response headers, log usage, alert near the limit, and back off. Aim for 5 or fewer calls to create/update an envelope.
- **API Usage Center** (Admin > Integrations > API Usage Center): calls by integration key, limit status, **efficiency scores**, and an **Update Hourly Limit** option.
- **Efficiency score factors**: blocked API calls; exceeded burst limit; exceeded hourly limit; excessive document retrieval requests; excessive envelope API requests; excessive envelope status requests; excessive recipient status requests; excessive requests for nonexistent envelopes; excessive requests per envelope; low call activity.
- Raising the limit yourself requires all of these: the plan includes limit management, you are an account admin, no Support-set limit is in effect, apps are efficient (fix the flagged issues first), and there is enough call history.

### Section 5 - Recipient authentication: comparison
| Method | How it is configured | Notes |
|---|---|---|
| Access code | `accessCode` on the recipient | Shared out of band. Lightest enforced method. |
| Phone (call or SMS) | `identityVerification.workflowId` (from `IdentityVerifications:list`) | Second factor. SMS can cost extra. |
| KBA | e.g. `idCheckConfigurationName` = "ID Check $" | Public-record questions, **US only**, LexisNexis. Heavy for low-risk documents. |
| ID verification (IDV) | `identityVerification.workflowId` (REST v2.1) | Government photo ID or eID. **Not enabled by default in demo**; ask the account manager. |
| Embedded record | `authenticationMethod` (+ `authenticationInstant`, `assertionId`, `securityDomain`) on `createRecipient` | **Records** your app's authentication on the certificate. It does **not enforce** anything. |
- All methods except IDV are enabled in demo, and production may cost extra. Match the method to the document's risk.
- Retrieve IDV evidence (ID images and events) with the **ID Evidence API**.

### Section 5 - EU Standards-Based Signatures (SBS)
- Signature types: electronic, **AES** (certificates from Docusign or your organization), and **QES** (from government-certified **QTSPs**).
- Add `recipientSignatureProviders` (`signatureProviderName` plus `signatureProviderOptions`, for example `oneTimePassword` or `sms`) to at least one signer in `Envelopes:create`.
- Available providers: `GET /restapi/v2.1/accounts/{accountId}/signatureProviders` (AccountSignatureProviders:list).
- **Not compatible with SBS**: attachment by fax, concatenating signer attachments, legacy digital signatures, Markup, Notary.
- **Works differently with SBS**:
  - Advanced Correct: no adding or deleting fields after the first signature.
  - Combined PDF download is **not** digitally signed.
  - Free-form signing: only signature and initials fields after someone has signed.
  - Watermarks are added as annotations.
  - Wet-signed documents are added as new documents.

### Section 5 - Web forms with vs. without an envelope
- **Template-based** configuration: built from an eSignature template (copied into a *web form template*). An **envelope is generated** after submission.
  - **Remote** instance: the envelope is created when `createInstance` is processed.
  - **Embedded** instance: the envelope is created when the **first user submits**.
- **Standalone** configuration: **no envelope**, data collection only. The `envelopes` array is empty.
- **Embedded** instances need `clientUserId` (max 100 characters) and render with the Docusign JS SDK.
- **Remote** instances use `sendOption` and `recipients[]` with `roleName`; users are reached by email.
- Prefill with `formValues`. Get field names from `Configurations:getForm`.
- Read results with `Instances:getInstance` / `listInstances`: `status` is INITIATED, INPROGRESS, SUBMITTED, EXPIRED or FAILED; also `instanceRecipientStatus`, `formValues` and `envelopes[]`.
- **Record of recipient authentication** (`authenticationMethod`, `authenticationInstant`, `assertionId`, `securityDomain` in `createInstance`): only for **embedded signing** of template-based forms. **Not supported** for remote instances or standalone configurations.

### Section 6 - Agreement Manager API: RAG and review
- Retrieve agreements and their AI-extracted data (parties, dates, provisions) with the Agreement Manager API (for example `getAgreement`).
- Index that data in your AI system's retrieval store, keyed by agreement ID, so answers can cite their source.
- Bulk-import legacy agreements so AI extraction runs on them too. Then review and correct the extractions (an external review step) before relying on them downstream.

### Section 7 - Workflow instance management (Maestro / Workflow Builder API)
- Base path: `https://api-d.docusign.com/v1` (demo) or `https://api.docusign.com/v1` (production). Scope: **`aow_manage`**, in addition to normal OAuth.
| Operation | Method and path |
|---|---|
| GetWorkflowsList | GET `/accounts/{accountId}/workflows` |
| GetWorkflowTriggerRequirements | GET `/workflows/{workflowId}/trigger-requirements` |
| TriggerWorkflow | POST `/workflows/{workflowId}/actions/trigger` |
| getWorkflowInstancesList | GET `/workflows/{workflowId}/instances` |
| **getWorkflowInstance** | GET `/workflows/{workflowId}/instances/{instanceId}` (status, start/end times, `started_by`) |
| cancelWorkflowInstance | POST `/instances/{instanceId}/actions/cancel` (stops one running instance) |
| pauseNewWorkflowInstances / resumePausedWorkflow | POST `/workflows/{workflowId}/actions/pause` or `resume` (affects **new** instances only) |
- Publishing runs an automated pre-publication check. If consent is missing, open the returned `consentUrl`, grant consent, and publish again (without `isPreRunCheck=true`).

### Section 8 - Extensions and extension points
| Extension | Extension point | Manifest value |
|---|---|---|
| Connected fields | eSignature Add Fields and signing | `ConnectedFields.Version1.Verify` (+ `DataIO.Version6.GetTypeNames` and `GetTypeDefinitions`) |
| Data IO | Maestro workflows | read/write system of record |
| Bank account owner verification | eSignature | `Verify.Version1.BankAccountOwner` (owner or authorized signatory; US ABA routing only) |
| Bank account verification | eSignature | `Verify.Version3.BankAccount` |
| Email / Phone verification | eSignature **and Web Forms** | `Verify.Version1.Email` / `Verify.Version1.PhoneNumber` |
| Business FEIN | eSignature | `Verify.Version1.BusinessEntity` |
| SSN, Postal address | eSignature | |
| File output cloud storage | Maestro workflows | use this for **new** apps (file archive is legacy) |
- Connected fields: when a connection is created or refreshed, Docusign calls Get Type Names, then Get Type Definitions (**Concerto** data model). Verify runs when the signer completes the required fields.
- Connected fields are **not supported in Maestro**.
- Sending by API: `TabInfo:GetConnectedFieldsTabGroups`, then put the data in each tab's `extensionData`, then `Envelopes:create`.
- Verification results come through the Connect **extension-executed** event (**JSON SIM only**), and also appear in envelope history and the certificate of completion.
- Org-specific verification usually belongs in a **private** extension app.
- Lifecycle: register (form or manifest) in the **Developer Console**, run connection and extension tests, run functional tests, then publish (public App Center review, or private).
