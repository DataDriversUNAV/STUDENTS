# =====================================================================
#  R Basics with the HCC Survival Data Set
#  Hepatocellular carcinoma (liver cancer): 165 patients, 49 features,
#  and a "Class" column (1 = survived 1 year, 0 = died).
#  Only base R is used, so nothing extra needs to be installed.
# =====================================================================

# ---- 1. Locate the data file -----------------------------------------
# Download the dataset first (from Kaggle, or with the Python kagglehub
# snippet), then set this to the folder that holds the files.
data_dir <- "C:/path/to/hcc-survival-data-set"   # <-- change this

files <- list.files(data_dir, pattern = "\\.(csv|txt)$", full.names = TRUE)
print(files)                      # see what files are available

# The original file "hcc-data.txt" has no header and uses "?" for missing values.
data_file <- files[grepl("hcc-data", basename(files))][1]
if (is.na(data_file)) data_file <- files[1]

# ---- 2. Load the data ------------------------------------------------
col_names <- c("Gender", "Symptoms", "Alcohol", "HBsAg", "HBeAg", "HBcAb",
               "HCVAb", "Cirrhosis", "Endemic", "Smoking", "Diabetes",
               "Obesity", "Hemochro", "AHT", "CRI", "HIV", "NASH", "Varices",
               "Spleno", "PHT", "PVT", "Metastasis", "Hallmark", "Age",
               "Grams_day", "Packs_year", "PS", "Encephalopathy", "Ascites",
               "INR", "AFP", "Hemoglobin", "MCV", "Leucocytes", "Platelets",
               "Albumin", "Total_Bil", "ALT", "AST", "GGT", "ALP", "TP",
               "Creatinine", "Nodule", "Major_Dim", "Dir_Bil", "Iron", "Sat",
               "Ferritin", "Class")

# If the first line contains letters it is a header row; otherwise use our names.
first_line <- readLines(data_file, n = 1)
has_header <- grepl("[A-Za-z]", first_line)

hcc <- read.csv(data_file, header = has_header, na.strings = c("?", "", "NA"))
if (!has_header && ncol(hcc) == length(col_names)) names(hcc) <- col_names

# ---- 3. First look ---------------------------------------------------
dim(hcc)          # rows and columns
head(hcc, 5)      # first 5 rows
str(hcc)          # type of every column
names(hcc)        # column names

# ---- 4. Missing values -----------------------------------------------
missing <- colSums(is.na(hcc))
sort(missing[missing > 0], decreasing = TRUE)   # columns with missing data
cat("Rows with no missing values:", sum(complete.cases(hcc)), "\n")

# ---- 5. Summary statistics -------------------------------------------
summary(hcc[, c("Age", "AFP", "Hemoglobin", "Albumin", "Platelets")])

mean(hcc$Age, na.rm = TRUE)
median(hcc$Age, na.rm = TRUE)
sd(hcc$Age, na.rm = TRUE)
range(hcc$Age, na.rm = TRUE)

# ---- 6. Factors and tables -------------------------------------------
# Turn the 0/1 outcome into a labeled factor.
hcc$Outcome <- factor(hcc$Class, levels = c(0, 1), labels = c("Died", "Survived"))
hcc$Gender  <- factor(hcc$Gender, levels = c(0, 1), labels = c("Female", "Male"))

table(hcc$Outcome)                       # counts
prop.table(table(hcc$Outcome))           # proportions
table(hcc$Gender, hcc$Outcome)           # two-way table

# ---- 7. Subsetting and filtering -------------------------------------
older <- hcc[hcc$Age >= 70 & !is.na(hcc$Age), ]
nrow(older)

alcohol_cirrhosis <- subset(hcc, Alcohol == 1 & Cirrhosis == 1,
                            select = c(Age, Gender, Outcome))
head(alcohol_cirrhosis)

# ---- 8. Group summaries ----------------------------------------------
aggregate(Age ~ Outcome, data = hcc, FUN = mean)
aggregate(cbind(Albumin, Hemoglobin) ~ Outcome, data = hcc, FUN = mean)
tapply(hcc$Total_Bil, hcc$Outcome, median, na.rm = TRUE)

# ---- 9. Creating a new variable --------------------------------------
hcc$AgeGroup <- cut(hcc$Age, breaks = c(0, 50, 65, 80, Inf),
                    labels = c("<50", "50-64", "65-79", "80+"), right = FALSE)
table(hcc$AgeGroup, hcc$Outcome)

# ---- 10. Simple plots ------------------------------------------------
par(mfrow = c(2, 2))   # 2 x 2 grid of plots

hist(hcc$Age, main = "Age distribution", xlab = "Age", col = "steelblue")

barplot(table(hcc$Outcome), main = "1-year outcome", col = c("tomato", "seagreen"))

boxplot(Albumin ~ Outcome, data = hcc, main = "Albumin by outcome",
        col = c("tomato", "seagreen"))

plot(hcc$Hemoglobin, hcc$Albumin, main = "Hemoglobin vs Albumin",
     xlab = "Hemoglobin", ylab = "Albumin",
     col = ifelse(hcc$Outcome == "Survived", "seagreen", "tomato"), pch = 19)

par(mfrow = c(1, 1))

# ---- 11. A first statistical test ------------------------------------
# Do survivors and non-survivors differ in albumin level?
t.test(Albumin ~ Outcome, data = hcc)

# Is survival associated with cirrhosis?
chisq.test(table(hcc$Cirrhosis, hcc$Outcome))

# ---- 12. A simple model ----------------------------------------------
# Logistic regression: predict survival from a few lab values.
model <- glm(Outcome ~ Age + Albumin + Total_Bil + Hemoglobin,
             data = hcc, family = binomial)
summary(model)

# ---- 13. Save a cleaned copy -----------------------------------------
write.csv(hcc, file.path(data_dir, "hcc_clean.csv"), row.names = FALSE)
cat("Done! Cleaned data saved to", file.path(data_dir, "hcc_clean.csv"), "\n")
