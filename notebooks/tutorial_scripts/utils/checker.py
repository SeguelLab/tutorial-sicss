from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score
import numpy as np

def test_metrics(y_true, y_pred, prec_in, rec_in, f1_in, acc_in):
    precision = precision_score(y_true=y_true, y_pred=y_pred)
    recall = recall_score(y_true=y_true, y_pred=y_pred)
    f1 = f1_score(y_true=y_true, y_pred=y_pred)
    acc = accuracy_score(y_true=y_true, y_pred=y_pred)
    
    ## TESTS ##
    try:
        assert np.isclose(precision, prec_in), f"\033[91mPrecision Test Failed. Precision should be {precision:.4f}.\033[0m"
        assert np.isclose(recall, rec_in), f"\033[91mRecall Test Failed. Recall should be {recall:.4f}.\033[0m"
        assert np.isclose(f1, f1_in), f"\033[91mF1 Test Failed. F1 should be {f1:.4f}.\033[0m"
        assert np.isclose(acc, acc_in), f"\033[91mAccuracy Test Failed. Accuracy should {acc:.4f}.\033[0m"
        ## Success ##
        print("\033[92mALL TESTS PASSED!\033[0m")
    except Exception as e:
        print(e)
    
 
