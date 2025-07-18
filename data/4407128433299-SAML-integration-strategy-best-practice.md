# SAML integration strategy & best practice

There are many ways to implement SAML to manage users and access OptiSigns with your IDP.

Here are some high-level best practices with OptiSigns that may help you to plan your integration and reduce overhead, and manual work later.

This article only focuses on the strategy & approach, for detailed step-by-step configuration, you can refer to [this guide](https://support.optisigns.com/hc/en-us/articles/4404590815635).

#### **Create a backup Admin account during set up:**

During set up, we recommend leaving Enable Username & Password login, and creating an Admin account with username/password to log back in and config, in case you accidentally lock yourself out by missing assignments of roles or groups.

You can disable this account later once your implementation is completed.

![mceclip0.png](https://support.optisigns.com/hc/article_attachments/4407128153235)

In this case, you are planning not to use email as the unique identifier for the user, and use a username or employee ID instead. We recommend having this on, so the account owner and admin account will be able to manage the account without interruption, e.g. forgetting the password, or an issue with identifying the provider.

#### **There are 2 Strategies for using SAML:**

**1) As an Authentication & Authorization Service** to enforce identity verification like above, but also enforce user, team, and role mapping in OptiSigns, With this approach you will map all users to groups in your IDP, and map the IDP groups to OptiSigns teams/roles. When there's a change in IDP like a user is added or moved group, it will automatically reflect in OptiSigns. **We recommend this approach**.

To implement this, check "Enable User Override", with this enabled, every time a user logs in using SAML, OptiSigns will check to see if their group assignment has changed, and enforce that accordingly, also if their name has changed, updated, it will also update OptiSigns.

![mceclip1.png](https://support.optisigns.com/hc/article_attachments/4407135779603)

Map all your appropriate groups to roles & team in OptiSigns.

For example we have 3 groups:

* Marketing West Coast - users responsible for managing screens, content for West region
* Marketing East Coast - user responsible for manage screens, content for East region
* IT Support - Admin that can support both region and do other admin tasks

The mapping should be like below.

![mceclip3.png](https://support.optisigns.com/hc/article_attachments/4407128634643)

With this set up, if a user belong to Marketing West Coast, later moved to Marketing East Coast, you just need to update your IDP move him/her from Marketing West Coast to Marketing East Coast, next time the user log in, he/she now belong to and can only see "Marketing West Coast" team content in OptiSigns.

**2) As Authentication Service Only** to enforce your MFA, Password policy, and remove user will no longer have access to OptiSigns. You will still can assigns, manage these users to Teams, Roles in OptiSigns. This approach is quick to set up and flexible as you can quickly move users around in OptiSigns, but when users moved around in your IDP, you will have to remember to move them around in OptiSigns as well, if that's a requirement.

To implement this, uncheck "Enable User Override"

![mceclip4.png](https://support.optisigns.com/hc/article_attachments/4407136124435)

This way, in the example above. When a user move from Marketing West Coast to Marketing East Coast.

You will need to go to OptiSigns and move the user's team assignment, if that's required.

Also if when the user update, change their name, you will have to update OptiSigns as well to keep it in sync.

#### **Enable User Creation:**

We recommend to keep this option checked. When this option is enabled, if users authenticated and SAML setting map the user to a team, role that can use OptiSigns, the user will be created automatically.

If disabled, you will have to create each user first in OptiSigns before they can log in with SAML SSO.

![mceclip5.png](https://support.optisigns.com/hc/article_attachments/4407136156819)

In the example above, if there are 20 users belong to Marketing West Coast group in your IDP, and Marketing West Coast is mapped to the Marketing West Coast team in OptiSigns.

If user A belong to Marketing West Coast group logs in, he/she will be created in OptiSigns and can start working right away to with West Coast Team screens and content.

The other 19 users are not created in OptiSigns until they attempt to log in.

You can also map the "Unmapped users/groups" to "No Team (Disable)", this way if a user belong to some other group in your IDP like say "Sales West Coast" try to log in, they will get an error and the user is not created in OptiSigns.

This way you can keep the system clean and only necessary users that using the app are replicated.

![mceclip6.png](https://support.optisigns.com/hc/article_attachments/4407136240659)

If you have any questions or need help with SAML integration please feel free to reach out to us at [support@optisigns.com](mailto:support@optisigns.com)