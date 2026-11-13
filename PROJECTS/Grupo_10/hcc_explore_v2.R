hcc <- read.csv(file.choose(), na.strings = "?")
# ---- 0. Paquetes y datos ---------------------------------------------
# install.packages("ggplot2")   # solo la primera vez
library(ggplot2)

# Leer los datos (los "?" del archivo pasan a NA)

df  <- hcc            # a partir de aquí se trabaja SOLO con df

# ---- 1. Quitar el prefijo "X<número>." ---------------------------------
names(df) <- sub("^X\\d+\\.", "", names(df))

# ---- 2. Desambiguar los nombres repetidos (por posición) ---------------
names(df)[4:6]       <- c("HBsAg", "HBeAg", "HBcAb")  # las tres "HepB"
names(df)[7]         <- "HCVAb"                      # "HepC"
names(df)[c(37, 46)] <- c("BilTot", "BilDir")         # bilirrubina total y directa

# ---- 3. Comprobar --------------------------------------------------------
anyDuplicated(names(df))   # debe dar 0
dim(df)                    # filas y columnas
head(df, 5)                # primeras 5 filas
str(df)                    # tipo de cada columna
names(df)                  # nombres de columnas

# ---- 4. Valores faltantes -----------------------------------------------
faltantes <- colSums(is.na(df))
sort(faltantes[faltantes > 0], decreasing = TRUE)   # columnas con NA
cat("Filas sin ningún NA:", sum(complete.cases(df)), "\n")

# ---- 5. Estadísticos descriptivos ---------------------------------------
summary(df$Agedia)

mean(df$Agedia, na.rm = TRUE)
median(df$Agedia, na.rm = TRUE)
sd(df$Agedia, na.rm = TRUE)
range(df$Agedia, na.rm = TRUE)

# ---- 6. Factores y tablas ------------------------------------------------
df$Outcome <- factor(df$Class, levels = c(0, 1), labels = c("Fallece", "Sobrevive"))
df$Gen     <- factor(df$Gen,   levels = c(0, 1), labels = c("Mujer", "Hombre"))

table(df$Outcome)                    # conteos
prop.table(table(df$Outcome))        # proporciones
table(df$Gen, df$Outcome)            # tabla cruzada

# ---- 7. Subconjuntos y filtros -------------------------------------------
mayores <- df[df$Agedia >= 70 & !is.na(df$Agedia), ]
nrow(mayores)

alcohol_cirrosis <- subset(df, Alc == 1 & Cir == 1,
                           select = c(Agedia, Gen, Outcome))
head(alcohol_cirrosis)

# ---- 8. Resúmenes por grupo ----------------------------------------------
aggregate(Agedia ~ Outcome, data = df, FUN = mean)
aggregate(cbind(Alb, Hae) ~ Outcome, data = df, FUN = mean)
tapply(df$BilTot, df$Outcome, median, na.rm = TRUE)

# ---- 9. Crear una variable nueva -----------------------------------------
df$GrupoEdad <- cut(df$Agedia, breaks = c(0, 50, 65, 80, Inf),
                    labels = c("<50", "50-64", "65-79", "80+"), right = FALSE)
table(df$GrupoEdad, df$Outcome)

# ---- 10. Gráficos básicos -------------------------------------------------
par(mfrow = c(2, 2))   # rejilla 2 x 2

hist(df$Agedia, main = "Distribución de edad", xlab = "Edad", col = "steelblue")

barplot(table(df$Outcome), main = "Desenlace al año",
        col = c("tomato", "seagreen"))

boxplot(Alb ~ Outcome, data = df, main = "Albúmina por desenlace",
        col = c("tomato", "seagreen"))

plot(df$Hae, df$Alb, main = "Hemoglobina vs Albúmina",
     xlab = "Hemoglobina", ylab = "Albúmina",
     col = ifelse(df$Outcome == "Sobrevive", "seagreen", "tomato"), pch = 19)

par(mfrow = c(1, 1))

# ---- 11. Primeros contrastes ----------------------------------------------
# ¿Difiere la albúmina entre los que sobreviven y los que fallecen?
t.test(Alb ~ Outcome, data = df)

# ¿Está asociada la supervivencia con la cirrosis?
chisq.test(table(df$Cir, df$Outcome))

# ---- 12. Modelo sencillo --------------------------------------------------
# Regresión logística: probabilidad de sobrevivir según algunos valores de laboratorio
modelo <- glm(Outcome ~ Agedia + Alb + BilTot + Hae,
              data = df, family = binomial)
summary(modelo)

# ---- 13. Guardar copia limpia ---------------------------------------------
write.csv(df, "hcc_clean.csv", row.names = FALSE)
cat("Listo. Datos guardados en hcc_clean.csv\n")

