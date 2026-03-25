# 🎓 Unidad 5: Reconocimiento de Imágenes - ÍNDICE DE ACCESO

**Estado**: ✅ Compilación exitosa y lista para aula

---

## 📚 Documentos Principales

### 1. 🎯 [Unidad5_Introduccion.html](Unidad5_Introduccion.html)
**Punto de entrada**: Overview de la Unidad 5
- Propósito y estructura modular
- Requisitos previos (Unidades 1-4)
- Flujo recomendado de estudio
- Competencias a desarrollar
- FAQ sobre algoritmos

**Duración sugerida**: 30-45 minutos lectura

---

### 2. 📖 [Unidad5_01_Algoritmos_Supervisados_NoSupervisados_handout.html](Unidad5_01_Algoritmos_Supervisados_NoSupervisados_handout.html)
**Teoría e implementación de algoritmos de aprendizaje automático**

**Contenido**:
- Regresión Logística
- Support Vector Machine (SVM)
- Árboles de Decisión
- Random Forest
- K-means
- Clustering Jerárquico
- PCA y t-SNE
- Pipelines en scikit-learn

**Duración sugerida**: 2-3 horas clase + ejercicios

---

### 3. 📊 [Unidad5_02_Evaluacion_Desempeno_handout.html](Unidad5_02_Evaluacion_Desempeno_handout.html)
**Evaluación rigurosa de modelos de clasificación**

**Contenido**:
- Matriz de confusión y métricas (Precisión, Recall, F1, AUC)
- Validación cruzada (k-Fold, Stratified, variantes)
- Curvas ROC y Precision-Recall
- Búsqueda de hiperparámetros (GridSearch, RandomSearch)
- Flujo completo de evaluación

**Duración sugerida**: 2 horas clase + ejercicios prácticos

---

### 4. 🔬 [ejemplo_real_Unidad5_clasificacion_flores_handout.html](ejemplo_real_Unidad5_clasificacion_flores_handout.html)
**Ejemplo reproducible completo de clasificación de imágenes**

**Flujo**:
1. Descargar dataset de flores (TensorFlow)
2. Extraer características (GLCM, Hu, Color)
3. Entrenar 5 modelos diferentes
4. Validación cruzada
5. Comparación de resultados
6. Análisis visual completo

**Duración sugerida**: 3-4 horas laboratorio

---

## 🔧 Recursos Complementarios

- **[README.md](README.md)**: Documentación detallada de archivos
- **[RESUMEN_EJECUTIVO.md](RESUMEN_EJECUTIVO.md)**: Resumen visual del diseño
- **[COMPILACION_VERIFICADA.md](COMPILACION_VERIFICADA.md)**: Reporte de compilación
- **[style.css](style.css)**: Estilos (automáticamente incluido)

---

## 📅 Planificación de Aula (Sugerida)

```
SEMANA 1:
  Lunes (2-3 hrs):
    - Lectura: Unidad5_Introduccion.html
    - Clase: Unidad5_01_Algoritmos (teoría)
    - Ejercicio: Implementar Logistic Regression y SVM
  
  Miércoles (2 hrs):
    - Clase: Unidad5_02_Evaluacion (métricas)
    - Ejercicio: Calcular F1, AUC, matriz de confusión
    - Demo: Validación cruzada

SEMANA 2:
  Lunes-Miércoles (3-4 hrs laboratorio):
    - Ejecutar: ejemplo_real_Unidad5
    - Probar: cambiar parámetros, K, max_depth
    - Visualizar: gráficos, ROC curves
    - Compare: múltiples algoritmos
  
  Viernes (Proyecto):
    - Estudiante trae dataset personal
    - Aplica flujo completo
    - Reporta: selección algoritmo + resultados
```

---

## 🚀 Cómo Usar

### Opción 1: Lectura en Navegador (Recomendado)
1. Abrir `Unidad5_Introduccion.html` en navegador
2. Leer índice y hacer click en documentos enlazados
3. Todos los HTML son self-contained (sin dependencias)

### Opción 2: Jupyter Notebook
Convertir a `.ipynb` y ejecutar en Jupyter/Colab:
```bash
quarto convert Unidad5_01_Algoritmos_Supervisados_NoSupervisados.qmd -t ipynb
```

### Opción 3: Edición Manual
Modificar archivos `.qmd` y renderizar nuevamente:
```bash
quarto render Unidad5_02_Evaluacion_Desempeno.qmd
```

---

## ✅ Verificación Rápida

- ✅ **Introducción**: Overview y estructura clara
- ✅ **Algoritmos**: 10+ técnicas documentadas con código
- ✅ **Evaluación**: Métricas completas y ejemplos
- ✅ **Ejemplo Real**: Dataset de flores, 5 modelos, comparación
- ✅ **HTML**: 4 archivos generados, 5.2 MB total
- ✅ **Estilos**: Consistente con Unidad 4
- ✅ **Documentación**: 3 archivos README/RESUMEN

---

## 📞 Soporte

### Si necesita...

**Cambiar contenido teórico**:
1. Abrir `.qmd` correspondiente
2. Editar en VS Code o editor de texto
3. `quarto render archivo.qmd`

**Agregar un nuevo algoritmo**:
1. Adicionar sección en Unidad5_01_Algoritmos
2. Incluir ecuación, implementación, ejemplo
3. Renderizar

**Crear versión PDF**:
```bash
quarto render Unidad5_01_Algoritmos_Supervisados_NoSupervisados.qmd -t pdf
```

**Adaptar a dataset local**:
1. Copiar código de `ejemplo_real_Unidad5`
2. Reemplazar ruta de datos
3. Ajustar extracción de características

---

## 📊 Contenido Sumario

| Documento | Secciones | Algoritmos | Ecuaciones | Código |
|----------|-----------|-----------|-----------|--------|
| Introducción | 10+ | - | - | - |
| Algoritmos | 20+ | 10+ | 10+ | 50+ |
| Evaluación | 15+ | - | 15+ | 20+ |
| Ejemplo Real | 12 | 5 | - | 30+ |

**Total**: 57+ secciones, 10+ algoritmos, 25+ ecuaciones, 100+ bloques código

---

## 🎓 Competencias después de Unidad 5

- Entrenar modelos supervisados (LR, SVM, RF, DT)
- Entrenar modelos no-supervisados (K-means, clustering)
- Evaluar con métricas rigurosas (F1, AUC, etc)
- Interpretar matrices de confusión y curvas ROC
- Evitar overfitting y data leakage
- Buscar hiperparámetros sistemáticamente
- Comparar modelos científicamente
- Implementar pipeline completo: imagen → predicción

---

<div style="text-align: center; margin-top: 2em;">

## 🎯 Estás listo para impartir Unidad 5

**Todos los documentos están compilados, verificados y listos para aula.**

</div>

---

*Compilado: 25 de marzo de 2026*
*Status: ✅ Listo para producción*
