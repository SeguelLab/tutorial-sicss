from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score
import numpy as np

def check_eval_metrics(y_true, y_pred, prec_in, rec_in, f1_in, acc_in):
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
    
 
