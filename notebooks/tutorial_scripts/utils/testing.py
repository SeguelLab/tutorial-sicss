from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score
import numpy as np

def check_eval_metrics(y_true, y_pred, prec_in: float, rec_in: float, f1_in: float, acc_in: float):
    """Takes two arrays of actual and predicted labels, and a set of precision, recall, f1, and accuracy measures.
    Then tests the provided values against functions from sklearn.metrics
    
    Args:
        y_true: Actual/True labels.
        y_pred: Predicted labels.
        prec_in (float): Precision to test.
        rec_in (float): Recall to test.
        f1_in (float): f1-score to test.
        acc_in (float): accuracy to test.
    """
    precision = precision_score(y_true=y_true, y_pred=y_pred)
    recall = recall_score(y_true=y_true, y_pred=y_pred)
    f1 = f1_score(y_true=y_true, y_pred=y_pred)
    acc = accuracy_score(y_true=y_true, y_pred=y_pred)
    
    ## TESTS ##
    try:
        assert np.isclose(precision, prec_in), f"\033[91mPrecision Test Failed. Precision should be {precision:.3f}, but got {prec_in:.3f}.\033[0m"
        assert np.isclose(recall, rec_in), f"\033[91mRecall Test Failed. Recall should be {recall:.3f}, but got {rec_in:.3f}.\033[0m"
        assert np.isclose(f1, f1_in), f"\033[91mF1 Test Failed. F1 should be {f1:.3f}, but got {f1_in:.3f}.\033[0m"
        assert np.isclose(acc, acc_in), f"\033[91mAccuracy Test Failed. Accuracy should be {acc:.3f}, but got {acc_in:.3f}.\033[0m"
        ## Success ##
        print("\033[92mALL TESTS PASSED!\033[0m")
    except Exception as e:
        print(e) 
    
 
