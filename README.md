***Getting AWS Account cost in Home-Assistant***

With this small tool you can deploy a Lambda to your AWS account that you want to monitor and a blueprint to your Home-Assistant setup to receive the current AWS cost in your HA.

*Prerequisites:*
1. A number input helper in your Home-Assistant
2. The HA Blueprint
3. Serverless Framework to deploy this stack
4. Your Home-Assistant instance is reachable over the internet

*Steps:*
1. Think of a random string for your webhook url, example : 648BjdhfSJdfhsufjdsf, write it down somewhere
2. Create a number helper in Home-Assistant (https://www.home-assistant.io/integrations/input_number/)
3. Import the blueprint from this Github repo
4. Create an automation from the blueprint, select the number helper and input the webhook_id that you've created
5. Copy the *config.example.json* file to *config.dev.json* and fill in the webhook URL, example : https://hass.mydomain.com/api/webhook/*<webhookid>*
6. Make sure you have your AWS credentials ready and tested with AWS CLI
7. Run *sls deploy* in this repository to deploy the code to your AWS account.
8. Done, every morning at 8AM the current AWS cost will be posted to your Home-Assistant helper!