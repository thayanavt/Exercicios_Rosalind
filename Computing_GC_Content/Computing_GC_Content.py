ids = []
G_list, C_list, percent_list, seqs_size_list  = [], [], [], []
seq= str()

with open("/home/thayana/Documentos/programas_python/ROSALIND/Computing_GC_Content/Computing_GC_Content.txt") as file_dna:
    for linha in file_dna:
        if not linha.startswith(">"):
            seq = seq + linha.rstrip("\n")
            
        else:
            ids.append(linha.replace('\n', '').replace('>', ''))
            seqs_size_list.append(len(seq))
            G_list.append(seq.count("G"))
            C_list.append(seq.count("C"))
            seq = str()

    seqs_size_list.append(len(seq))
    G_list.append(seq.count("G"))
    C_list.append(seq.count("C"))

seqs_size_list.remove(seqs_size_list[0])
G_list.remove(G_list[0])
C_list.remove(C_list[0])

for G, C, seq_size in zip(G_list, C_list, seqs_size_list):
    percent_list.append(((G+C)/seq_size) * 100)

max_percent_index = percent_list.index(max(percent_list))

print(ids[max_percent_index])
print(percent_list[max_percent_index])