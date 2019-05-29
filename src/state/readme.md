# Azure CLI State Extension #
This is an extension to azure cli that allows for environmental scanning for Azure RBAC, Policy, locks, and resource structure.

The extension simplifies the querying process and will provide a summary of access, policies, locks, as well as a hierarchy of resources.

## How to use ##
First, install the extension:
```
az extension add --name scan
```

Then, call it as you would any other az command:
```
az state
```


Other options and examples of using the extensions can be viewed with the help command:
```
az state --help
```