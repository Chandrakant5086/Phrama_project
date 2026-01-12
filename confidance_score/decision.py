from  utils.logger import log 
from  confidance_score.confi_score import calculate_confidence

def make_decision(confidence_score):
    if confidence_score >= 0.75:
        return "ANSWER"
    elif confidence_score >= 0.50:
        return "ANSWER_WITH_WARNING"
    else:
        return "REFUSE"



