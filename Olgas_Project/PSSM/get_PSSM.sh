cd ./train
for my_queries in *.fasta

do psiblast -query $my_queries -db ../uniprot_sprot.fasta -evalue 0.001 -num_iterations 3 -out_ascii_pssm ./$my_queries.pssm -out ./$my_queries.psiblast


done
