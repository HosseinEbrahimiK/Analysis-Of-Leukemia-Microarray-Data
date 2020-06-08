setwd("~/Desktop/project/")

library(Biobase)
library(GEOquery)
library(limma)
library(pheatmap)
library(gplots)
library(ggplot2)
library(reshape2)
library(tidyr)
library(dplyr)
library(plyr)

gset <- getGEO(GSEMatrix=TRUE, filename = "data/GSE48558_series_matrix.txt.gz", AnnotGPL=TRUE, destdir = "data/")

gr1 <- c(rep('AML', 40), "Normal", rep('AML', 3), "Normal", rep("AML", 23), "Normal", "AML", "Normal", rep("AML", 3), "Normal", "AML", rep("Normal", 4), "AML", "Normal", "AML", "AML", "Normal","Normal", "AML", "AML", "Normal", "Normal", "AML", "Normal", "AML", "Normal", "AML", "Normal", "AML", "Normal", "AML",  "Normal", rep("AML", 3), "Normal", rep("AML", 3), "Normal", rep("AML", 29), rep("Normal", 7),"AML", "AML", "Normal", rep("AML", 3), rep("Normal", 20))
gr2 <- c(rep('AML', 13), rep("AML", 4), rep("AML", 2), "AML", "AML","AML", "AML", "AML", "AML", "AML", rep("AML", 2), rep("AML", 5), "AML", "AML", "AML", "AML", "AML", "AML","AML", "G", "AML", "AML", "AML", "G", "AML", "AML", "AML", "AML", rep("AML", 2), "AML",rep("AML", 2), "AML", rep("AML", 2), "AML", "AML", "AML", "AML", "AML", "AML", "AML", "AML", "AML", "AML", "AML", "B", "AML", "T", "AML", "AML", "AML", "G", "AML", "G", "M", "M", "B", "AML", "T", "AML", "AML", rep("T", 2), "AML", "AML", rep("T", 2), "AML", "B", "AML", "T", "AML", "B", "AML", "T", "AML", "cd34", "AML", "AML","AML", "cd34", "AML", "AML","AML", "cd34", "AML", "AML", "AML", "AML", rep("AML", 9), "AML", rep("AML", 7), rep("AML", 8), rep("G", 7), "AML", "AML", "T", rep("AML", 3), rep("B", 7), "T", rep("M", 4), "G", rep("T", 7))
gr3 <- c(rep('AMLP', 13), rep("B_ALL", 4), rep("T_ALL", 2), "B_ALL", "T_ALL","B_ALL", "B_ALL", "T_ALL", "B_ALL", "B_ALL", rep("T_ALL", 2), rep("B_ALL", 5), "T_ALL", "T_ALL", "B_ALL", "T_ALL", "BP", "T_ALL","AMLCL", "G", "BP", "T_ALL", "AMLCL", "G", "BP", "T_ALL", "AMLCL", "BP", rep("AMLCL", 2), "BP",rep("AMLCL", 2), "BP", rep("AMLCL", 2), "BP", "B_ALL", "AMLCL", "BP", "B_ALL", "AMLCL", "BP", "B_ALL", "AMLCL", "BP", "B_ALL", "B", "B_ALL", "T", "AMLCL", "BP", "B_ALL", "G", "B_ALL", "G", "M", "M", "B", "B_ALL", "T", "AMLCL", "B_ALL", rep("T", 2), "AMLCL", "B_ALL", rep("T", 2), "AMLCL", "B", "B_ALL", "T", "AMLCL", "B", "B_ALL", "T", "AMLCL", "cd34", "T_ALL", "TP","AMLCL", "cd34", "T_ALL", "TP","AMLCL", "cd34", "T_ALL", "TP", "AMLCL", "TP", rep("BP", 9), "TP", rep("BP", 7), rep("TP", 8), rep("G", 7), "AMLP", "AMLP", "T", rep("AMLP", 3), rep("B", 7), "T", rep("M", 4), "G", rep("T", 7))
gr4 <- c(rep('AMLP', 13), rep("B_ALL", 4), rep("T_ALL", 2), "B_ALL", "T_ALL","B_ALL", "B_ALL", "T_ALL", "B_ALL", "B_ALL", rep("T_ALL", 2), rep("B_ALL", 5), "T_ALL", "T_ALL", "B_ALL", "T_ALL", "BP", "T_ALL","AMLCL", "Normal", "BP", "T_ALL", "AMLCL", "Normal", "BP", "T_ALL", "AMLCL", "BP", rep("AMLCL", 2), "BP",rep("AMLCL", 2), "BP", rep("AMLCL", 2), "BP", "B_ALL", "AMLCL", "BP", "B_ALL", "AMLCL", "BP", "B_ALL", "AMLCL", "BP", "B_ALL", "Normal", "B_ALL", "Normal", "AMLCL", "BP", "B_ALL", "Normal", "B_ALL", "Normal", "Normal", "Normal", "Normal", "B_ALL", "Normal", "AMLCL", "B_ALL", rep("Normal", 2), "AMLCL", "B_ALL", rep("Normal", 2), "AMLCL", "Normal", "B_ALL", "Normal", "AMLCL", "Normal", "B_ALL", "Normal", "AMLCL", "Normal", "T_ALL", "TP","AMLCL", "Normal", "T_ALL", "TP","AMLCL", "Normal", "T_ALL", "TP", "AMLCL", "TP", rep("BP", 9), "TP", rep("BP", 7), rep("TP", 8), rep("Normal", 7), "AMLP", "AMLP", "Normal", rep("AMLP", 3), rep("Normal", 7), "Normal", rep("Normal", 4), "Normal", rep("Normal", 7))

ex <- exprs(gset)
## scale of ex is logarithmic, otherwise we should perform: ex <- log2(ex + 1) and exprs(gset) <- ex

pdf("Results/plotNo1.pdf", width = 15, height = 10)
boxplot(ex, color=redblue(256))
dev.off()
## data is already normolized, otherwise we should perform this command : ex <- normalizedQuantiles(ex) and exprs(gset) <- ex

pdf("Results/pheatmap.pdf", width = 20, height = 20)
pheatmap(cor(ex), labels_row = gr3, labels_col = gr3, color = bluered(256), border_color = NA)
dev.off()

pc.row <- prcomp(ex)
pdf("Results/PC_row.pdf")
plot(pc.row)
dev.off()

pdf("Results/data_row_pc.pdf")
plot(pc.row$x[,1:2])
dev.off()

ex.scale <- t(scale(t(ex), scale = F))
pc <- prcomp(ex.scale)
pdf("Results/PC_scaled.pdf")
plot(pc)
dev.off()

pdf("Results/data_scaled_pc.pdf")
plot(pc$x[,1:2])
dev.off()

pcr <- data.frame(pc$rotation[,1:3], Group=gr4)
pdf("Results/PCA_samples.pdf")
ggplot(pcr, aes(PC1, PC2, color=Group)) + geom_point(size=3) + theme_bw()
dev.off()

gr4 <- factor(gr4)
gset$description <- gr4
design <- model.matrix(~ description + 0, gset)
colnames(design) <- levels(gr4)
fit <- lmFit(gset, design)
cont.matrix <- makeContrasts(AML-Normal, levels = design)
fit2 <- contrasts.fit(fit, cont.matrix)
fit2 <- eBayes(fit2, 0.01)
tT <- topTable(fit2, adjust="fdr", sort.by="B", number = Inf)

tT <- subset(tT, select=c("Gene.symbol", "Gene.ID", "adj.P.Val", "logFC"))
write.table(tT, file="Results/AML_Normal.txt", row.names = F, sep = "\t", quote = F)

aml.up <- subset(tT, logFC > 1 & adj.P.Val < 0.05)
aml.up.genes <- unique(aml.up$Gene.symbol)
aml.up.genes <- unique(as.character(strsplit2(aml.up.genes, "///")))
write.table(aml.up.genes, file="Results/AML_Normal_up.txt", quote = F, row.names = F, col.names = F)

aml.down <- subset(tT, logFC < -1 & adj.P.Val < 0.05)
aml.down.genes <- unique(aml.down$Gene.symbol)
aml.down.genes <- unique(as.character(strsplit2(aml.down.genes, "///")))
write.table(aml.down.genes, file="Results/AML_Normal_down.txt", quote = F, row.names = F, col.names = F)
