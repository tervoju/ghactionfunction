import logging

import azure.functions as func

app = func.FunctionApp()

@app.event_grid_trigger(arg_name="azeventgrid")
def EventGridTriggerTrialToo(azeventgrid: func.EventGridEvent):
    logging.info('Python EventGrid trigger processed an event')
