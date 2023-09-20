# diary-entry-api
A [DRF](https://www.django-rest-framework.org/) API for a diary entry application

## Features
  a. Users can register, log in and log out of the application. They should also be able to reset their password
  |    Method     |  Endpoint                    | Public Access |
  | :------------:|:----------------------------:|:-------------:|
  | POST          | /auth/register               | TRUE          |
  | POST          | /auth/login                  | TRUE          |
  | POST          | /auth/logout                 | FALSE         |
  | POST          | /auth/reset-password         | FALSE         |

  b. Enable users to create, update, view and delete a diary
  |    Method      |         Endpoint               | Public Access |
  | :-------------:| ------------------------------:|:-------------:|
  | GET            | /diaries/                      | FALSE         |
  | GET            | /diaries/<id>                  | FALSE         |
  | POST           | /diaries/                      | FALSE         |
  | PUT            | /diaries/<id>                  | FALSE         |
  | DELETE         | /diaries/<id>                  | FALSE         |

  b. Add, update, view or delete entries in a diary
  |    Method      |         Endpoint                 | Public Access |
  :---------------:|:--------------------------------:|:-------------:|
  | GET            | /diaries/<id>/entries            | FALSE         |
  | GET            | /diaries/<id>/entries/<id>       | FALSE         |
  | POST           | /diaries/<id>/entries            | FALSE         |
  | PUT            | /diaries/v1/entries/<id>         | FALSE         |
  | DELETE         | /diaries/v1/entries/<id>         | FALSE         |

