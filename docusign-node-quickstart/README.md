# Docusign Node Quickstart

This folder contains the Node.js Docusign Quickstart project extracted from:

`C:\Users\Admin\Downloads\Quickstart App-1-node.js.zip`

The actual application source is in:

`docusign-node-quickstart/app`

## Safety Note

The copied `app/config/appsettings.json` and `app/config/private.key` files were removed after extraction because they can contain real credentials. Use `app/config/appsettings.example.json` as the template when you want to run the app locally.

## Run

```powershell
cd "D:\Docusign exam\docusign-node-quickstart\app"
npm install
Copy-Item config\appsettings.example.json config\appsettings.json
npm start
```

Then fill `config/appsettings.json` with your local Docusign developer settings before starting the app.
