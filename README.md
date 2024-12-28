# SleepAPI

A small flask API I use with HomeAssistant. Allows setting Sleep or Shutdown states on PC via POST request

### HomeAssistant integration:

To integrate into HA, open up your configuration.yaml and add the following;

``` yaml
rest_command:
  sleep_button:
    url: http://DEVICE_IP:PORT/sleep
    method: POST
    headers:
      Content-Type: "application/json"
    payload: "{}"

  shutdown_button:
    url: http://DEVICE_IP:PORT/shutdown
    method: POST
    headers:
      Content-Type: "application/json"
    payload: "{}"

```

Next, we need to add a script which we can call to use the above commands. Simply open up your scripts.yaml on your HA instance or create the helper via the UI.

``` yaml
thinClientSleep:
  alias: Sleep Thin Client
  sequence:
    - service: rest_command.sleep_button
  mode: single

thinClientShutdown:
    alias: Shutdown Thin Client
    sequence:
        - service: rest_command.shutdown_button
    mode: single

  ```

Finally, restart the Home Assistant server. Open up your dashboard and add the new integrations. DONE, now you too can sleep and shutdown your PC via a button press on Home Assistant