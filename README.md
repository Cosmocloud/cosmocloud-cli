# Cosmocloud CLI

Cosmocloud CLI is a command line interface for [Cosmocloud Deploy](https://cosmocloud.io). It allows you to interact with Cosmocloud Deploy from the command line.

## Installation

To install the [Cosmocloud CLI](https://pypi.org/project/cosmocloud/), run the following command:

```sh
pip install cosmocloud
```

## Usage

Here are some commands you can use for managing your App Services in Cosmocloud Deploy -

- [Login](#login)
- [List Organisations](#list-organisations)
- [List App Services in an Organisation](#list-app-services-in-an-organisation)
- [Get list of Releases for App Service](#get-list-of-releases-for-app-service)
- [Release a new version for an App Service](#release-a-new-version-for-an-app-service)
- [Promote a Release to another Environment](#promote-a-release-to-another-environment)

### Login

To log in to your Cosmocloud account, use the following command:

```sh
cosmocloud login --username <username> --password <password>
```

If successful, you should see a meesage such as -

```sh
Login successful!
```

If you see any other error messages, please check the message and follow the instructions.

### List Organisations

To list the organisations you have access to, use the following command:

```sh
cosmocloud list-organisations
```

This will return a list of organisations you have access to, along with their active status, such as -

```sh
TestOrg : ACTIVE
AnotherOrg : ACTIVE
SampleBusiness : INACTIVE
```

### List App Services in an Organisation

To list the app services in a specific organisation, use the following command:

```sh
cosmocloud list-app-services --organisation <organisation_name>
```

This will return a list of app services in the specified organisation, such as -

```sh
AppService1 : ACTIVE
AppService2 : ACTIVE
AppService3 : INACTIVE
```

### Get list of Releases for App Service

To get a list of releases for a specific app service, use the following command:

```sh
cosmocloud list-releases --organisation <organisation_name> --app-service <app_service_name>
```

### Release a new version for an App Service

To release a new version for an app service, use the following command:

```sh
cosmocloud release --organisation <organisation_name> --app-service <app_service_name> --version <version_number> --environment <environment_name>
```

You can only releases a version **once** for an app service. If you try to release the same version again, you will see an error message.

You can **promote** an existing release to another environment, by using the promote command.

### Promote a Release to another Environment

To promote a release to another environment, use the following command:

```sh
cosmocloud promote --organisation <organisation_name> --app-service <app_service_name> --version <version_number> --environment <environment_name>
```

If there is no version existing already, you will see an error message.

## Help and Support

If you need help or support, please contact us at [contact@cosmocloud.io](mailto:contact@cosmocloud.io).

You can also join our [Cosmocloud Discord Server](https://discord.gg/M8gqTVpRYE) for instant support.
