![Power Automate flow, commented, without this image this post will be pretty confusing.](/assets/images/updating-on-call-schedule-using-power-automate/flowcommented.png)


This was a straightforward one in the end, but it took several attempts at different automation technologies (Azure Automation, Function Apps were tried and the amount of time investment required was steep), and then testing out multiple steps in Power Automate before I landed on it.

The screenshot I've posted is commented with the individual steps taken.

The BIG caveat is that Power Automate only supports updating Security Groups using the Azure AD connector. That's right, you can't use Microsoft 365 Groups, nor Distribution Groups, nor Mail-enabled Security Groups.. only Security Groups.

We are using Microsoft Teams Calling, and have set up a call queue for our on call schedule - this currently rotates through three different staff members internally on a three week schedule. The call queue does not support setting a schedule natively, updating it manually each week was becoming a pain, and could easily be forgotten, especially if I was away, or started late, or it was simply just missed. So I decided it was time to automate, less than two hours later I was done, and here I am posting it on Reddit.
