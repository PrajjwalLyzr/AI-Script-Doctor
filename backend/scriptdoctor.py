from lyzr_automata import Task, Agent
from lyzr_automata.ai_models.openai import OpenAIModel
from lyzr_automata.tasks.task_literals import InputType, OutputType
from lyzr_automata.pipelines.linear_sync_pipeline  import  LinearSyncPipeline
from lyzr_automata import Logger



def openai_text(ApiKey):
    open_ai_model_text = OpenAIModel(
    api_key= ApiKey,
    parameters={
        "model": "gpt-4o",
        "temperature": 0.5,
        "max_tokens": 1500,
    })

    return open_ai_model_text


def AIScriptDoctor(apikey, script):
    ai_script_doctor = Agent(
        prompt_persona=""" As an AI Script Doctor, you are expert into enhance the storytelling by identifying plot holes, pacing issues, and suggesting improvements to elevate your film and TV scripts. Let's refine your narrative for a compelling and cohesive story. """,
        role="AI Script Doctor",
    )


    identify_plot_holes = Task(
        name="Identify Plot Holes",
        agent=ai_script_doctor,
        output_type=OutputType.TEXT,
        input_type=InputType.TEXT,
        model=openai_text(ApiKey=apikey),
        instructions=f"""Identify plot holes in the following script:\n{script}""",
        log_output=True,
        enhance_prompt=False,
        default_input=script
    )

    identify_pacing_issues = Task(
        name="Identify Pacing Issues",
        agent=ai_script_doctor,
        output_type=OutputType.TEXT,
        input_type=InputType.TEXT,
        model=openai_text(ApiKey=apikey),
        instructions=f"""Identify pacing issues in the following script:\n{script}""",
        log_output=True,
        enhance_prompt=False,
        default_input=script
    )

    suggest_improvements = Task(
        name="Suggested Improvments",
        agent=ai_script_doctor,
        output_type=OutputType.TEXT,
        input_type=InputType.TEXT,
        model=openai_text(ApiKey=apikey),
        instructions=f"""Suggest improvements for the following script:\n{script}""",
        log_output=True,
        enhance_prompt=False,
        default_input=script
    )

    logger = Logger()
    
    improvedScript = LinearSyncPipeline(
        logger=logger,
        name="AI Script Improver",
        completion_message="Improved the Script Successfully !",
        tasks=[
            identify_plot_holes,
            identify_pacing_issues,
            suggest_improvements
        ],
    ).run()

    return improvedScript