# Final Predictor

Within this folder you will find scripts and saved models, as well FASTA files. More specifically: 

 	For running SVM without PSSM:
	
	•	RUN: run_my_SVM_model_test_set.py, which unzips the SVM_new_model.pkl.zip file and tests the model on
	89 sequences from the file test_final.txt (/Datasets). The output is a Confusion Matrix, and a text file
	my_final_predictions.txt, which will contain:
			Protein ID,
			Sequence,
			True Topology,
			Predicted Topology
		
 	For running SVM with PSSM:
	
	•	RUN: Test_my_model_PSSM.py, which unzips the file my_pssm_SVM_final.pkl.zip, the test_final.zip and 
	train_final.tar.xz folders, which contain the FASTA files for the test and train sequences, as well as the 
	PSSM matrices. Then the model is tested over the test set of the 89 sequences by using the evolutionary 
	information deriving from the PSSM matrices.The output is a Confusion Matrix and a text file
	true_vs_predicted_topo_SVM_PSSM_final.txt, which will contain:
			Protein ID,
			Sequence,
			True Topology,
			Predicted Topology.
		
Complementary files and scripts:

	Parsers_windows.py: Extract protein IDs, features and sequences for every single sequence and gives an 
	SVM input as a final output (is imported as a module for the SVM model test python script).

	PSSM_parsing.py: Parses the PSSM output for every single sequence and gives an SVM input as a final 
	output (is imported as a module for the PSSM-based SVM model test python script).

For running a simple (without PSSM data) SVM on 50 new proteins:

	new_family_proteins.py: for parsing protein IDs and features. 

	50_new folder: Contains FASTA files and PSSMs deriving from PSI- BLAST for 
	50 proteins of unknown topology.

	New_50_proteins_SVM.py: calls the SVM_new_model.pkl model and predicts the topology of these proteins. 
	Final output is a txt file with the name predicted_topo_50_New_prot.txt.


	
