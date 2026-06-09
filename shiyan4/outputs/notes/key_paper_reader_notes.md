# 重点论文阅读笔记

说明：本文件按 nature-reader 的“源文件定位 + 结构化阅读”思想建立，但任务目标是技术调研而非全文翻译，因此保留题名、来源、关键段落线索和人工综合笔记，不复制整篇论文正文。

## P13 Segment Anything SAM

- 选择理由：SAM 原始模型，提供 promptable segmentation 与 SA-1B 数据引擎，是所有适配方案的技术起点。
- 本地文件：`眼底视网膜病变分割-论文PDF/SAM相关/2023_Segment_Anything_SAM_arXiv2304.02643.pdf`
- 类别/方向：SAM相关 / 通用 SAM / 高质量或快速分割
- 年份与标识：2023；arXiv:2304.02643
- 自动抽取数据集线索：COCO; LVIS; SA-1B
- 自动抽取损失/训练线索：Focal loss; dice loss; focal loss
- 方法关键词：Prompt; SAM; Sam; Transformer; cross-attention; decoder; encoder; gaze; prompt; self-attention; transformer

### 结构化阅读线索

**abstract**

```text
Abstract We introduce the Segment Anything (SA) project: a new task, model, and dataset for image segmentation. Using our efﬁcient model in a data collection loop, we built the largest segmentation dataset to date (by far), with over 1 billion masks on 11M licensed and privacy respecting images. The model is designed and trained to be promptable, so it can transfer zero-shot to new image distributions and tasks. We evaluate its capabilities on numerous tasks and ﬁnd that its zero-shot performance is impressive – often competitive with or even superior to prior fully supervised results. We are releasing the Segment Anything Model (SAM) and corresponding dataset (SA-1B) of 1B masks and 11M images at https://segment-anything.com to foster research into foundation models for computer vision. 1.
```

**method**

```text
method for zero-shot transfer to downstream segmentation tasks via prompting. Pre-training. The promptable segmentation task suggests a natural pre-training algorithm that simulates a sequence of prompts (e.g., points, boxes, masks) for each training sample and compares the model’s mask predictions against the ground truth. We adapt this method from interactive segmentation [109, 70], although unlike interactive segmentation whose aim is to eventually predict a valid mask after enough user input, our aim is to always predict a valid mask for any prompt even when the prompt is ambiguous. This ensures that a pre-trained model is effective in use cases that involve ambiguity, including automatic annotation as required by our data engine §4. We note that performing well at this task is challenging and requires specialized modeling and training loss choices, which we discuss in §3. Zero-shot transfer. Intuitively, our pre-training task endows the model with the ability to respond appropriately to any prompt at inference time, and thus downstream tasks can be solved by engineering appropriate prompts. For example, if one has a bounding box detector for cats, cat instance segmentation can be solved by providing the detector’s box output as a prompt to our model. In general, a wide array of practical segmentation tasks can be cast as prompting. In addition to automatic dataset labeling, we explore ﬁve diverse example tasks in our
```

**experiment**

```text
experiments that demonstrate the effectiveness of our approach. Task (§2). In NLP and more recently computer vision, foundation models are a promising development that can perform zero-shot and few-shot learning for new datasets and tasks often by using “prompting” techniques. Inspired by this line of work, we propose the promptable segmentation task, where the goal is to return a valid segmentation mask given any segmentation prompt (see Fig. 1a). A prompt simply speciﬁes what to segment in an image, e.g., a prompt can include spatial or text information identifying an object. The requirement of a valid output mask means that even when a prompt is ambiguous and could refer to multiple objects (for example, a point on a shirt may indicate either the shirt or the person wearing it), the output should be a reasonable mask for at least one of those objects. We use the promptable segmentation task as both a pre-training objective and to solve general downstream segmentation tasks via prompt engineering. Model (§3). The promptable segmentation task and the goal of real-world use impose constraints on the model architecture. In particular, the model must support ﬂexible prompts, needs to compute masks in amortized real-time to allow interactive use, and must be ambiguity-aware. Surprisingly, we ﬁnd that a simple design satisﬁes all three constraints: a powerful image encoder computes an image embedding, a prompt encoder embeds prompts, and then the two information sources are combined in a lightweight mask decoder that predicts segmentation masks. We refer to this model as the Se
```

**conclusion**

```text
Discussion. Prompting and composition are powerful tools that enable a single model to be used in extensible ways, potentially to accomplish tasks unknown at the time of model design. This approach is analogous to how other foundation models are used, e.g., how CLIP [82] is the text-image alignment component of the DALL·E [83] image generation system. We anticipate that composable system design, powered by techniques such as prompt engineering, will enable a wider variety of applications than systems trained specifically for a ﬁxed set of tasks. It’s also interesting to compare promptable and interactive segmentation through the lens of composition: while interactive segmentation models are designed with human users in mind, a model trained for promptable segmentation can also be composed into a larger algorithmic system as we will demonstrate. 4 , score score score , , valid masks image image encoder image embedding mask points box text prompt encoder mask decoder conv Figure 4: Segment Anything Model (SAM) overview. A heavyweight image encoder outputs an image embedding that can then be efﬁciently queried by a variety of input prompts to produce object masks at amortized real-time speed. For ambiguous prompts corresponding to more than one object, SAM can output multiple valid masks and associated conﬁdence scores. 3. Segment Anything Model We next describe the Segment Anything Model (SAM) for promptable segmentation. SAM has three components, illustrated in Fig. 4: an image encoder, a ﬂexible prompt encoder, and a fast mask decoder. We build on Transformer vision models 
```

### 人工综合要点

- 研究问题：见后续 `key_paper_analysis.md` 的人工归纳表。
- 方法、数据集、指标、优势、不足和可借鉴点：在后续综合表中统一给出，避免仅凭 PDF 自动抽取片段下结论。

## P09 MedSAM Segment Anything in Medical Images

- 选择理由：MedSAM，代表大规模医学图像微调路线，可作为医学 SAM 适配的主线背景。
- 本地文件：`眼底视网膜病变分割-论文PDF/SAM相关/2023_MedSAM_Segment_Anything_in_Medical_Images_arXiv2304.12306.pdf`
- 类别/方向：SAM相关 / 医学 SAM / 医学图像适配
- 年份与标识：2023；arXiv:2304.12306
- 自动抽取数据集线索：未抽取
- 自动抽取损失/训练线索：Dice loss; cross-entropy; dice loss
- 方法关键词：Encoder; MedSAM; Prompt; SAM; Sam; cross-attention; decoder; encoder; knowledge distillation; prompt; sam; self-attention; transformer

### 结构化阅读线索

**abstract**

```text
Abstract Medical image segmentation is a critical component in clinical practice, facilitating accurate diagnosis, treatment planning, and disease monitoring. However, existing methods, often tailored to specific modalities or disease types, lack generalizability across the diverse spectrum of medical image segmentation tasks. Here we present MedSAM, a foundation model designed for bridging this gap by enabling universal medical image segmentation. The model is developed on a large-scale medical image dataset with 1,570,263 image-mask pairs, covering 10 imaging modalities and over 30 cancer types. We conduct a comprehensive evaluation on 86 internal validation tasks and 60 external validation tasks, demonstrating better accuracy and robustness than modality-wise specialist models. By delivering accurate and efficient segmentation across a wide spectrum of tasks, MedSAM holds significant potential to expedite the evolution of diagnostic tools and the personalization of treatment plans. 1 arXiv:2304.12306v3 [eess.IV] 1 Apr 2024
```

**method**

```text
methods, often tailored to specific modalities or disease types, lack generalizability across the diverse spectrum of medical image segmentation tasks. Here we present MedSAM, a foundation model designed for bridging this gap by enabling universal medical image segmentation. The model is developed on a large-scale medical image dataset with 1,570,263 image-mask pairs, covering 10 imaging modalities and over 30 cancer types. We conduct a comprehensive
```

**experiment**

```text
evaluation on 86 internal validation tasks and 60 external validation tasks, demonstrating better accuracy and robustness than modality-wise specialist models. By delivering accurate and efficient segmentation across a wide spectrum of tasks, MedSAM holds significant potential to expedite the evolution of diagnostic tools and the personalization of treatment plans. 1 arXiv:2304.12306v3 [eess.IV] 1 Apr 2024 Introduction Segmentation is a fundamental task in medical imaging analysis, which involves identifying and delineating regions of interest (ROI) in various medical images, such as organs, lesions, and tissues [1]. Accurate segmentation is essential for many clinical applications, including disease diagnosis, treatment planning, and monitoring of disease progression [2, 3]. Manual segmentation has long been the gold standard for delineating anatomical structures and pathological regions, but this process is timeconsuming, labor-intensive, and often requires a high degree of expertise. Semi- or fully-automatic segmentation methods can significantly reduce the time and labor required, increase consistency, and enable the analysis of large-scale datasets [4]. Deep learning-based models have shown great promise in medical image segmentation due to their ability to learn intricate image features and deliver accurate segmentation results across a diverse range of tasks, from segmenting specific anatomical structures to identifying pathological regions [5]. However, a significant limitation of many current medical image segmentation models is their task-specific nature. These mo
```

**conclusion**

```text
Discussion We introduce MedSAM, a deep learning-powered foundation model designed for the segmentation of a wide array of anatomical structures and lesions across diverse medical imaging modalities. MedSAM is trained on a meticulously assembled large-scale dataset comprised of over one million medical image-mask pairs. Its promptable configuration strikes an optimal balance between automation and customization, rendering MedSAM a versatile tool for universal medical image segmentation. Through comprehensive evaluations encompassing both internal and external validation, MedSAM has demonstrated substantial capabilities in segmenting a diverse array of targets and robust generalization abilities to manage new data and tasks. Its performance not only significantly exceeds that of existing the state-of-the-art segmentation foundation model, but also rivals or even surpasses specialist models. By providing precise delineation of anatomical structures and pathological regions, MedSAM facilitates the computation of various quantitative measures that serve as biomarkers. For instance, in the field of oncology, MedSAM could play a crucial role in accelerating the 3D tumor annotation process, enabling subsequent calculations of tumor volume, which is a critical biomarker [29] for assessing disease progression and response to treatment. Additionally, MedSAM provides a successful paradigm for adapting natural image foundation models to new domains, which can be further extended to biological image segmentation [30], such as cell segmentation in light microscopy images [31] and organell
```

### 人工综合要点

- 研究问题：见后续 `key_paper_analysis.md` 的人工归纳表。
- 方法、数据集、指标、优势、不足和可借鉴点：在后续综合表中统一给出，避免仅凭 PDF 自动抽取片段下结论。

## P10 Medical SAM Adapter

- 选择理由：Medical SAM Adapter，代表参数高效 adapter/提示适配路线。
- 本地文件：`眼底视网膜病变分割-论文PDF/SAM相关/2023_Medical_SAM_Adapter_arXiv2304.12620.pdf`
- 类别/方向：SAM相关 / 医学 SAM / 医学图像适配
- 年份与标识：2023；arXiv:2304.12620
- 自动抽取数据集线索：未抽取
- 自动抽取损失/训练线索：未抽取
- 方法关键词：Adapter; MedSAM; Prompt; SAM; Transformer; adapter; cross-attention; decoder; encoder; prompt; sam; self-attention; transformer

### 结构化阅读线索

**abstract**

```text
Abstract The Segment Anything Model (SAM) has recently gained popularity in the field of image segmentation due to its impressive capabilities in various segmentation tasks and its prompt-based interface. However, recent studies and individual experiments have shown that SAM underperforms in medical image segmentation, since the lack of the medical specific knowledge. This raises the question of how to enhance SAM’s segmentation capability for medical images. In this paper, instead of fine-tuning the SAM model, we propose the Medical SAM Adapter (Med-SA), which incorporates domain-specific medical knowledge into the segmentation model using a light yet effective adaptation technique. In Med-SA, we propose Space-Depth Transpose (SD-Trans) to adapt 2D SAM to 3D medical images and Hyper-Prompting Adapter (HyP-Adpt) to achieve prompt-conditioned adaptation. We conduct comprehensive evaluation experiments on 17 medical image segmentation tasks across various image modalities. Med-SA outperforms several state-of-the-art (SOTA) medical image segmentation methods, while updating only 2% of the parameters. Our code is released at https: //github.com/KidsWithTokens/Medical-SAM-Adapter.
```

**method**

```text
methods, while updating only 2% of the parameters. Our code is released at https: //github.com/KidsWithTokens/Medical-SAM-Adapter. Introduction Very recently, the Segmentation Anything Model (SAM) (Kirillov et al. 2023) has gained significant attention as a powerful and versatile vision segmentation model. It can generate diverse and detailed segmentation masks based on user prompts. Despite its strong performance over natural images, many recent studies also show (Deng et al. 2023; Roy et al. 2023; He et al. 2023) that it reaches subpar performance on medical image segmentation. Making medical image segmentation interactive, such as employing techniques like SAM, holds immense clinical value. An interactive system can prioritize areas of interest as indicated by the clinicians, providing them with a more immersive and personalized experience. For instance, in a single fundus image, there are often overlapping and intricately intertwined structures such as vessels, optic disc, optic cup, and macula. Interactive segmentation can greatly assist clinicians in efficiently distinguishing target tissues from these complex structures. Considering the difficulty in acquiring large-scale annotated datasets, it becomes crucial to adopt a foundational interactive model like SAM for clinical utilization. SAM’s limited performance on medical images is due to its lack of medical-specific knowledge, including challenges like low image contrast, ambiguous tissue boundaries, and tiny lesion regions. The state-of-the-art (SOTA) approach to address this issue is fully fine-tuning the vanilla 
```

**experiment**

```text
experiments have shown that SAM underperforms in medical image segmentation, since the lack of the medical specific knowledge. This raises the question of how to enhance SAM’s segmentation capability for medical images. In this paper, instead of fine-tuning the SAM model, we propose the Medical SAM Adapter (Med-SA), which incorporates domain-specific medical knowledge into the segmentation model using a light yet effective adaptation technique. In Med-SA, we propose Space-Depth Transpose (SD-Trans) to adapt 2D SAM to 3D medical images and Hyper-Prompting Adapter (HyP-Adpt) to achieve prompt-conditioned adaptation. We conduct comprehensive evaluation experiments on 17 medical image segmentation tasks across various image modalities. Med-SA outperforms several state-of-the-art (SOTA) medical image segmentation methods, while updating only 2% of the parameters. Our code is released at https: //github.com/KidsWithTokens/Medical-SAM-Adapter. Introduction Very recently, the Segmentation Anything Model (SAM) (Kirillov et al. 2023) has gained significant attention as a powerful and versatile vision segmentation model. It can generate diverse and detailed segmentation masks based on user prompts. Despite its strong performance over natural images, many recent studies also show (Deng et al. 2023; Roy et al. 2023; He et al. 2023) that it reaches subpar performance on medical image segmentation. Making medical image segmentation interactive, such as employing techniques like SAM, holds immense clinical value. An interactive system can prioritize areas of interest as indicated by the cl
```

**conclusion**

```text
Conclusion In this paper, we have extended SAM, a powerful general segmentation model, to address medical image segmentation, introducing Med-SA. Leveraging parameter-efficient adaptation with simple yet effective SD-Trans and HyP- Adpt, we have achieved substantial improvements over the original SAM model. Our approach has resulted in SOTA performance across 17 medical image segmentation tasks spanning 5 different image modalities. We anticipate that this work will serve as a stepping stone towards advancing foundation medical image segmentation and inspire the development of novel fine-tuning techniques.
```

### 人工综合要点

- 研究问题：见后续 `key_paper_analysis.md` 的人工归纳表。
- 方法、数据集、指标、优势、不足和可借鉴点：在后续综合表中统一给出，避免仅凭 PDF 自动抽取片段下结论。

## P11 SAM-Med2D

- 选择理由：SAM-Med2D，代表 2D 医学 SAM 大数据集、多提示微调路线。
- 本地文件：`眼底视网膜病变分割-论文PDF/SAM相关/2023_SAM-Med2D_arXiv2308.16184.pdf`
- 类别/方向：SAM相关 / 医学 SAM / 医学图像适配
- 年份与标识：2023；arXiv:2308.16184
- 自动抽取数据集线索：Breast Ultrasound; SA-1B
- 自动抽取损失/训练线索：Focal loss; boundary loss; dice loss; focal loss
- 方法关键词：Adapter; Decoder; Encoder; MedSAM; Prompt; SAM; Sam; Transformer; adapter; cross-attention; decoder; encoder; prompt; sam; transformer

### 结构化阅读线索

**abstract**

```text
Abstract The Segment Anything Model (SAM) represents a state-of-the-art research advancement in natural image segmentation, achieving impressive results with input prompts such as points and bounding boxes. However, our evaluation and recent research indicate that directly applying the pretrained SAM to medical image segmentation does not yield satisfactory performance. This limitation primarily arises from significant domain gap between natural images and medical images. To bridge this gap, we introduce SAM-Med2D, the most comprehensive studies on applying SAM to medical 2D images. Its comprehensiveness manifests in three aspects: the comprehensive analysis on collecting the largest medical data, the most comprehensive studies on various fine-tuning options, the most comprehensive evaluation on the performance. Specifically, we first collect and curate approximately 4.6M images and 19.7M masks from public and private datasets, constructing a large-scale medical image segmentation dataset encompassing various modalities and objects. Then, we comprehensively fine-tune SAM on this dataset and turn it into SAM-Med2D. Unlike previous methods that only adopt bounding box or point prompts as interactive segmentation approach, we adapt SAM to medical image segmentation through more comprehensive prompts involving bounding boxes, points, and masks. We additionally fine-tune the encoder and decoder of the original SAM to obtain a well-performed SAM-Med2D, leading to the most comprehensive fine-tuning strategies to date. Finally, we conducted a comprehensive evaluation and analysis t
```

**method**

```text
methods that only adopt bounding box or point prompts as interactive segmentation approach, we adapt SAM to medical image segmentation through more comprehensive prompts involving bounding boxes, points, and masks. We additionally fine-tune the encoder and decoder of the original SAM to obtain a well-performed SAM-Med2D, leading to the most comprehensive fine-tuning strategies to date. Finally, we conducted a comprehensive
```

**experiment**

```text
evaluation and recent research indicate that directly applying the pretrained SAM to medical image segmentation does not yield satisfactory performance. This limitation primarily arises from significant domain gap between natural images and medical images. To bridge this gap, we introduce SAM-Med2D, the most comprehensive studies on applying SAM to medical 2D images. Its comprehensiveness manifests in three aspects: the comprehensive analysis on collecting the largest medical data, the most comprehensive studies on various fine-tuning options, the most comprehensive evaluation on the performance. Specifically, we first collect and curate approximately 4.6M images and 19.7M masks from public and private datasets, constructing a large-scale medical image segmentation dataset encompassing various modalities and objects. Then, we comprehensively fine-tune SAM on this dataset and turn it into SAM-Med2D. Unlike previous methods that only adopt bounding box or point prompts as interactive segmentation approach, we adapt SAM to medical image segmentation through more comprehensive prompts involving bounding boxes, points, and masks. We additionally fine-tune the encoder and decoder of the original SAM to obtain a well-performed SAM-Med2D, leading to the most comprehensive fine-tuning strategies to date. Finally, we conducted a comprehensive evaluation and analysis to investigate the performance of SAM-Med2D in medical image segmentation across various modalities, anatomical structures, and organs. Concurrently, we validated the generalization capability of SAM-Med2D on 9 datasets f
```

**conclusion**

```text
conclusion that SAM-Med2D exhibits excellent performance in the segmentation tasks across different anatomical structures, yielding satisfactory results in terms of the Dice metric in the pelvic and thoracic areas. However, it is worth noting that the performance of the head and neck region appears to be relatively subpar across different models and resolutions, suggesting the need for additional improvement measures. Table 3: Segmentation performance in point prompt mode. The left values represent Dice scores of different models under 1 pt prompt. The numbers in parentheses indicate the Dice score increment after 5 pts prompt, with red indicating improvement and green indicating decline. Modal SAM [8] SAM [8] FT-SAM SAM-Med2D (256 × 256) (1024 × 1024) (256 × 256) (256 × 256) CT 20.87(∆18.62) 48.36(∆12.74) 67.91(∆13.81) 77.34(∆6.75) MR 15.25(∆18.41) 16.45(∆7.07) 46.36(∆18.17) 57.16(∆12.02) PET 15.12(∆25.09) 34.52(∆8.93) 59.58(∆11.58) 78.58(∆2.42) Dermoscopy 58.01(∆10.01) 55.28(∆11.38) 83.86(∆6.82) 87.69(∆4.34) Endoscopy 39.94(∆13.84) 56.92(∆10.64) 57.17(∆20.56) 60.34(∆12.13) Fundus 33.67(∆28.50) 22.99(∆27.93) 62.57(∆14.62) 76.86(∆6.51) Histopathology 36.55(∆31.92) 79.96(↓0.20) 79.70(∆7.99) 76.89(∆4.31) Microscopy 44.92(∆15.05) 78.98(↓0.55) 70.27(∆13.63) 60.83(∆13.50) Ultrasound 15.89(∆14.51) 15.81(∆19.85) 55.05(∆23.46) 74.81(∆10.33) X-ray 23.40(∆11.04) 23.12(∆16.56) 44.06(∆25.84) 64.30(∆12.13) C. Performance Evaluation on Different Modalities. Figure 5 (b) summarizes the performance of the four methods under the Bbox prompt mode across different modality data. All four meth
```

### 人工综合要点

- 研究问题：见后续 `key_paper_analysis.md` 的人工归纳表。
- 方法、数据集、指标、优势、不足和可借鉴点：在后续综合表中统一给出，避免仅凭 PDF 自动抽取片段下结论。

## P15 SAM 2 Segment Anything in Images and Videos

- 选择理由：SAM 2，代表图像/视频统一和记忆机制，对连续眼底随访和高效提示有启发。
- 本地文件：`眼底视网膜病变分割-论文PDF/SAM相关/2024_SAM_2_Segment_Anything_in_Images_and_Videos_arXiv2408.00714.pdf`
- 类别/方向：SAM相关 / 通用 SAM / 高质量或快速分割
- 年份与标识：2024；arXiv:2408.00714
- 自动抽取数据集线索：LVIS; SA-1B
- 自动抽取损失/训练线索：cross-entropy; dice loss
- 方法关键词：Prompt; SAM; adapter; cross-attention; decoder; encoder; prompt; sam; self-attention; transformer

### 结构化阅读线索

**abstract**

```text
未抽取到稳定片段。
```

**method**

```text
method, and all frames require mask annotation from scratch, the process is slow, with an average annotation time of 37.8 seconds per frame in our
```

**experiment**

```text
evaluation of SAM 2 indicates minimal performance discrepancy in video segmentation based on perceived gender, and little variance among the three perceived age groups we evaluated. Our experiments (§6) show that SAM 2 delivers a step-change in the video segmentation experience. SAM 2 can produce better segmentation accuracy while using 3× fewer interactions than prior approaches. Further, SAM 2 outperforms prior work in established video object segmentation benchmarks, under multiple evaluation settings, and delivers better performance compared to SAM on image segmentation benchmarks, while being 6× faster. SAM 2 is shown to be effective across a variety of video and image distributions as observed through numerous zero-shot benchmarks including 17 for video segmentation and 37 for single-image segmentation. We are releasing our work under permissive open licences, including the SA-V dataset (CC by 4.0), the SAM 2 model checkpoints1, training code (Apache 2.0), and code for our interactive online demo (Apache 2.0). 2 Related work Image segmentation. Segment Anything (Kirillov et al., 2023) introduces a promptable image segmentation task where the goal is to output a valid segmentation mask given an input prompt such as a bounding box or a point that refers to the object of interest. SAM trained on the SA-1B dataset allows for zero-shot segmentation which enabled its adoption to a wide range of applications. Recent work has extended SAM, e.g., by introducing a High-Quality output token to train on fine-grained masks (Ke et al., 2024), or improve SAM’s efficiency (Xiong et a
```

**conclusion**

```text
Conclusion We present a natural evolution of Segment Anything into the video domain, based on three key aspects: (i) extending the promptable segmentation task to video, (ii) equipping the SAM architecture to use memory when applied to video, and (iii) the diverse SA-V dataset for training and benchmarking video segmentation. We believe SAM 2 marks a significant advancement in visual perception, positioning our contributions as milestones that will propel further research and applications. Acknowledgements. We thank Alexander Kirillov and Jitendra Malik for discussions on project direction. Thanks to Andrew Huang, Sahir Gomez, Miguel Martin, Devansh Kukreja, and Somya Jain for work on the demo, and to Aohan Lin and Meng Wang for creating the dataset visualizer. We thank Shoubhik Debnath and Sagar Vaze for their work on dataset preparation. Thanks also to William Ngan and Sasha Mitts for their design expertise and to Grant Gardner and George Orlin for leading product management. We are grateful to Joelle Pineau, Daniel Bolya, Kate Saenko, Pengchuan Zhang, and Christopher Chedeau, for valuable discussions. Thanks to Rene Martinez Doehner and Baishan Guo for data support, and to our annotation engineering and management partners: Robert Kuo, Rishi Godugu, Bob Kamma, Ida Cheng, Claudette Ward, Kai Brown, Jake Kinney, Jenny Truong, and Karen Bergan. Thanks to Vispi Cassod, Parth Malani, Shiva Koduvayur, Alexander Miller, and Caleb Ho for their support with compute and infra. Finally, we thank Azita Shokrpour, Mallika Malhotra, Rodrick Shepard, Jonathan Torres, Luc Dahlin, David 
```

### 人工综合要点

- 研究问题：见后续 `key_paper_analysis.md` 的人工归纳表。
- 方法、数据集、指标、优势、不足和可借鉴点：在后续综合表中统一给出，避免仅凭 PDF 自动抽取片段下结论。

## P23 RTNet Relation Transformer Network for DR Multi-lesion Segmentation

- 选择理由：RTNet，代表眼底 DR 多病灶分割中利用病灶-血管关系和 transformer 的专用模型。
- 本地文件：`眼底视网膜病变分割-论文PDF/眼底视网膜病变分割/2022_RTNet_Relation_Transformer_Network_for_DR_Multi-lesion_Segmentation_arXiv2201.11037.pdf`
- 类别/方向：眼底视网膜病变分割 / 眼底 DR 病灶分割
- 年份与标识：2022；arXiv:2201.11037
- 自动抽取数据集线索：DDR; IDRID; IDRiD; Idrid; idrid
- 自动抽取损失/训练线索：cross-entropy
- 方法关键词：CLAHE; CROSS-ATTENTION; Encoder; SELF-ATTENTION; Transformer; cross-attention; decoder; encoder; self-attention; transformer

### 结构化阅读线索

**abstract**

```text
Abstract— Automatic diabetic retinopathy (DR) lesions segmentation makes great sense of assisting ophthalmologists in diagnosis. Although many researches have been conducted on this task, most prior works paid too much attention to the designs of networks instead of considering the pathological association for lesions. Through investigating the pathogenic causes of DR lesions in advance, we found that certain lesions are closed to speciﬁc vessels and present relative patterns to each other. Motivated by the observation, we propose a relation transformer block (RTB) to incorporate attention mechanisms at two main levels: a self-attention transformer exploits global dependencies among lesion features, while a cross-attention transformer allows interactions between lesion and vessel features by integrating valuable vascular information to alleviate ambiguity in lesion detection caused by complex fundus structures. In addition, to capture the small lesion patterns ﬁrst, we propose a global transformer block (GTB) which preserves detailed information in deep network. By integrating the above blocks of dual-branches, our network segments the four kinds of lesions simultaneously. Comprehensive experiments on IDRiD and DDR datasets well demonstrate the superiority of our approach, which achieves competitive performance compared to state-of-the-arts. Index Terms— Diabetic retinopathy, Fundus image, Semantic segmentation, Transformer, Deep learning I.
```

**method**

```text
our method achieves a front row ﬁnish on DR multi-lesion segmentation. Speciﬁcally, our method achieves the best performance in exduates segmentation and ranks second in HE lesion segmentation.
```

**experiment**

```text
experiments on IDRiD and DDR datasets well demonstrate the superiority of our approach, which achieves competitive performance compared to state-of-the-arts. Index Terms— Diabetic retinopathy, Fundus image, Semantic segmentation, Transformer, Deep learning I. INTRODUCTION D IABETIC retinopathy (DR) has become a worldwide major medical concern for the large population of diabetic patients and has been the leading cause of blindness in the working-age population today [1]–[3]. DR lesions often present as microaneurysms (MAs), hemorrhages (HEs), soft exudates (SEs), and hard exudates (EXs) which can be observed in colorful fundus images and are the basis of diagnosis for ophthalmologists. However, until now there has been no valid treatment to cure this disease completely. The most recognized treatment is the early diagnosis and intervention to controll the progression of the disease and to avoid eventual loss of vision [4]. Thus, many national health institutions are promoting DR screening, which has been proven effective in reducing the rate of blindness caused by DR [2], [5]. However, screening is a heavy burden This work was supported by the Key Laboratory Foundation under Grant TCGZ2020C004 and Grant 202020429036. Shiqi Huang, Jianan Li, Yuze Xiao, Ning Shen and Tingfa Xu are with Beijing Institute of Technology, China. Tingfa Xu is also with Chongqing Innovation Center, Beijing Institute of Technology, China (email: huangsq, ciom xtf1, lijianan@bit.edu.cn). Corresponding authors: Tingfa Xu and Jianan Li. Fig. 1. Illustration of fundus image with characteristics of DR les
```

**conclusion**

```text
CONCLUSION AND DISCUSSION In this paper, we present a novel network that employs a dual-branch architecture with GTB and RTB to segment the four DR lesions simultaneously. Outstanding experiment results of our network can be attributed to GTB and RTB, which investigate the intra-class dependencies among multilesion and inter-class relations of multi-lesion and vessels. However, limited to the considerable cost of expertise pixellevel annotations, the vessel pseudo masks provided by semisupervised learning are inevitably coarse-grained and lead to the inadequacy of our network. Therefore, in our future work, we will further modify the vascular semi-supervised learning strategy and keep improving the transformer structures to achieve better performance in DR multi-lesion segmentation with less memory requirement.
```

### 人工综合要点

- 研究问题：见后续 `key_paper_analysis.md` 的人工归纳表。
- 方法、数据集、指标、优势、不足和可借鉴点：在后续综合表中统一给出，避免仅凭 PDF 自动抽取片段下结论。

## P25 GlanceSeg Microaneurysm Lesion Segmentation

- 选择理由：GlanceSeg，代表 gaze/saliency prompt + SAM 处理微小微动脉瘤的眼底场景适配。
- 本地文件：`眼底视网膜病变分割-论文PDF/眼底视网膜病变分割/2023_GlanceSeg_Microaneurysm_Lesion_Segmentation_arXiv2311.08075.pdf`
- 类别/方向：眼底视网膜病变分割 / 眼底 DR 病灶分割
- 年份与标识：2023；arXiv:2311.08075
- 自动抽取数据集线索：IDRID; IDRiD; Idrid; RETINAL-LESIONS; Retinal-Lesions; idrid
- 自动抽取损失/训练线索：未抽取
- 方法关键词：Gaze; MedSAM; SAM; adapter; decoder; gaze; prompt; saliency; sam; transformer

### 结构化阅读线索

**abstract**

```text
Abstract—Early-stage diabetic retinopathy (DR) presents challenges in clinical diagnosis due to inconspicuous and minute microangioma lesions, resulting in limited research in this area. Additionally, the potential of emerging foundation models, such as the segment anything model (SAM), in medical scenarios remains rarely explored. In this work, we propose a humanin-the-loop, label-free early DR diagnosis framework called GlanceSeg, based on SAM. GlanceSeg enables real-time segmentation of microangioma lesions as ophthalmologists review fundus images. Our humanin-the-loop framework integrates the ophthalmologist’s gaze map, allowing for rough localization of minute lesions in fundus images. Subsequently, a saliency map is generated based on the located region of interest, which provides prompt points to assist the foundation model in efﬁciently segmenting microangioma lesions. Finally, a domain knowledge ﬁlter reﬁnes the segmentation of minute lesions. We conducted experiments on two newly-built public datasets, i.e., IDRiD and Retinal- Lesions, and validated the feasibility and superiority of GlanceSeg through visualized illustrations and quantitative measures. Additionally, we demonstrated that GlanceSeg improves annotation efﬁciency for clinicians and enhances segmentation performance through ﬁne-tuning using annotations. This study highlights the potential of GlanceSeg-based annotations for self-model optimization, leading to enduring performance advancements through This work was supported in part by General Program of National Natural Science Foundation of China under
```

**method**

```text
framework called GlanceSeg, based on SAM. GlanceSeg enables real-time segmentation of microangioma lesions as ophthalmologists review fundus images. Our humanin-the-loop framework integrates the ophthalmologist’s gaze map, allowing for rough localization of minute lesions in fundus images. Subsequently, a saliency map is generated based on the located region of interest, which provides prompt points to assist the foundation model in efﬁciently segmenting microangioma lesions. Finally, a domain knowledge ﬁlter reﬁnes the segmentation of minute lesions. We conducted
```

**experiment**

```text
experiments on two newly-built public datasets, i.e., IDRiD and Retinal- Lesions, and validated the feasibility and superiority of GlanceSeg through visualized illustrations and quantitative measures. Additionally, we demonstrated that GlanceSeg improves annotation efﬁciency for clinicians and enhances segmentation performance through ﬁne-tuning using annotations. This study highlights the potential of GlanceSeg-based annotations for self-model optimization, leading to enduring performance advancements through This work was supported in part by General Program of National Natural Science Foundation of China under Grant 82272086, Shenzhen Science and Technology Program under Grant KQTD20180412181221912 and Grant JCYJ20200109140603831, the Innovation and Technology Fund (ITF) of Hong Kong SAR (ITS/240/21), and the Science, Technology, and Innovation Commission (STIC) of Shenzhen Municipality (SGDX20220530111005039). Hongyang Jiang, Xiaoqing Zhang, and Jiang Liu are with the Department of Computer Science and Engineering, Southern University of Science and Technology, Shenzhen, China. (e-mail: jianghy3@sustech.edu.cn; 11930927@mail.sustech.edu.cn; liuj@sustech.edu.cn). Zirong Liu, Chen Tang, and Jiang Liu are with the School of Ophthalmology and Optometry and Eye Hospital, Wenzhou Medical University, Wenzhou 325027, China. (e-mail: zirongliu98@qq.com; tangchen419@163.com; liuj@sustech.edu.cn). Shuai Jiang is with Intelligent Vision Plus Technology Co., Ltd., Shenzhen, China. (e-mail: jsiacb@foxmail.com). Mengdi Gao and Wu Yuan are with the Department of Biomedical Engineering,
```

**conclusion**

```text
DISCUSSION A. Ablation study GlanceSeg, grounded on the foundation model SAM, enables unsupervised real-time segmentation of retinal microangioma lesions in fundus images. GlanceSeg primarily consists of three core modules: gaze map-guided coarse segmentation of peri-microangiomal regions, microangioma segmentation via saliency map-generated prompt points based on the SAM model, and further segmentation reﬁnement utilizing domain knowledge ﬁlter. Gaza maps of ophthalmologists during fundus image interpretation contribute to roughly localize the region of tiny lesions, narrowing the segmentation scope and ensuring real-time segmentation. Due to the remarkably small size of microangioma lesions, it is unfeasible to accomplish lesion segmentation under unsupervised conditions using the SAM model without the beneﬁt of gaze maps. Then, ablation studies were conducted to demonstrate the effectiveness of prompt points derived from the saliency map and optimization of segmentation outcomes using the domain knowledge ﬁlter. Fig. 8(a) and (b) individually showcase the Precision/Recall curves for three ablation experiments conducted on IDRiD and Retinal-Lesions datasets. From Fig. 8(a), the SAM group refers to the results obtained following an initial segmentation process based on the gaze map, utilizing 200×200 evenly distributed sampling points as prompt points for further segmentation. The introduction of prompt points derived from the saliency map has improved the SAM model’s performance, with the AUPR increasing from 0.1762 to 0.2296. Furthermore, the domain knowledge ﬁlter group
```

### 人工综合要点

- 研究问题：见后续 `key_paper_analysis.md` 的人工归纳表。
- 方法、数据集、指标、优势、不足和可借鉴点：在后续综合表中统一给出，避免仅凭 PDF 自动抽取片段下结论。

## P21 Improving Lesion Segmentation for Diabetic Retinopathy

- 选择理由：IDRiD 病灶分割基线与对抗学习，体现早期针对小病灶/边缘的分割损失设计。
- 本地文件：`眼底视网膜病变分割-论文PDF/眼底视网膜病变分割/2020_Improving_Lesion_Segmentation_for_Diabetic_Retinopathy_arXiv2007.13854.pdf`
- 类别/方向：眼底视网膜病变分割 / 眼底 DR 病灶分割
- 年份与标识：2020；arXiv:2007.13854
- 自动抽取数据集线索：IDRiD; Messidor
- 自动抽取损失/训练线索：adversarial loss; cross entropy; cross-entropy
- 方法关键词：CGAN; CLAHE; HEDNet; cGAN

### 结构化阅读线索

**abstract**

```text
Abstract. Diabetic Retinopathy (DR) is a leading cause of blindness in working age adults. DR lesions can be challenging to identify in fundus images, and automatic DR detection systems can oﬀer strong clinical value. Of the publicly available labeled datasets for DR, the Indian Diabetic Retinopathy Image Dataset (IDRiD) presents retinal fundus images with pixel-level annotations of four distinct lesions: microaneurysms, hemorrhages, soft exudates and hard exudates. We utilize the HEDNet edge detector to solve a semantic segmentation task on this dataset, and then propose an end-to-end system for pixel-level segmentation of DR lesions by incorporating HEDNet into a Conditional Generative Adversarial Network (cGAN). We design a loss function that adds adversarial loss to segmentation loss. Our experiments show that the addition of the adversarial loss improves the lesion segmentation performance over the baseline. Keywords: Conditional Generative Adversarial Networks · Deep Learning · Segmentation · Medical Image Analysis.
```

**method**

```text
methods save time and can reduce uncertainty in DR diagnosis. The datasets available for DR strongly inﬂuence development of automated detection algorithms. Publicly available datasets for DR, such as Messidor [1], DRIVE [2], STARE [3] and DIARETDB [4], contain annotations of the whole image or of sub-regions of the image. Unfortunately, detection algorithms built from these datasets tend to make image level or patch level predictions, which by design has limited utility to a clinician who needs to explain the underlying factors leading to the diagnosis. A system capable of accurate pixel-level segmentation is more explainable and provides better value to clinicians. In this work, we use the Indian Diabetic Retinopathy Image Dataset (IDRiD) [5]. To the best of our knowledge, IDRiD is the ﬁrst public database for DR containing pixel level annotations of four typical DR lesions: microaneurysms (MA), hemorrhages (HE), hard exudates (EX), and soft exudates (SE). Physicians assess combinations of these lesions to diagnose various grades of DR. Fig. 1. Color fundus photograph containing diﬀerent retinal lesions associated with diabetic retinopathy. Enlarged parts illustrating presence of Microaneurysms, Soft Exudates, Hemorrhages and Hard Exudates. Our method uses the Holistically-Nested Edge Detection (HEDNet) network [7] to compute a segmentation map from a fundus image. To enhance HEDNet segmentation performance, we incorporate this model into a conditional Generative Adversarial Network (GAN) with a standard PatchGAN discriminator. Our method is end-to-end, and we show that t
```

**experiment**

```text
experiments show that the addition of the adversarial loss improves the lesion segmentation performance over the baseline. Keywords: Conditional Generative Adversarial Networks · Deep Learning · Segmentation · Medical Image Analysis. 1 Introduction Diabetic Retinopathy (DR) is an eye disease caused by damage to the retinal blood vessels of diabetic patients. Since the disease is relatively asymptomatic until the patient experiences loss of vision, physicians recommend regular screenings for diabetic patients. Analysis of high resolution fundus images obtained during the screening requires considerable time and eﬀort by trained clinicians, as lesions can be hard to detect. While the diagnosis of the disease ultimately requires a physician, automated detection of DR lesions can improve patient outcomes. Recent developments in machine learning and computer vision that enable accurate classiﬁcation and localization are well suited to the DR detection task. Of particular interest are arXiv:2007.13854v1 [eess.IV] 27 Jul 2020 2 Q. Xiao et al. pixel level annotations of DR lesions that suggest to physicians where in the image the lesions should be. Automated detection methods save time and can reduce uncertainty in DR diagnosis. The datasets available for DR strongly inﬂuence development of automated detection algorithms. Publicly available datasets for DR, such as Messidor [1], DRIVE [2], STARE [3] and DIARETDB [4], contain annotations of the whole image or of sub-regions of the image. Unfortunately, detection algorithms built from these datasets tend to make image level or patch 
```

**conclusion**

```text
Conclusion In this paper we have presented a method to improve the lesion segmentation performance on retinal images. We propose to use HEDNet to segment lesions in retinal images and, then, retinal image and segmentation pairs are fed to a PatchGAN discriminator that is trained to distinguish between ground truth pairs and predicted ones. The HEDNet segmentation model is then trained to both minimize a segmentation loss and to maximize the discriminator classiﬁcation loss. 10 Q. Xiao et al. Fig. 4. Top: An example test set image presenting all four lesion types. Bottom: Segmentation maps. Each row, from top to bottom, shows lesion types: MA, SE, EX and HE. Each column, from left to right, contains segmentation maps of ground truth, HEDNet output, and HEDNet + cGAN output, respectively. Improving Lesion Segmentation for Diabetic Retinopathy using Adversarial Learning 11 By using this approach, we show that it is possible to improve average precision on all lesion segmentation tasks. In particular, the AP of SE and HE segmentation improves by 5.3 and 3.1 percentage points when using conditional GANs over using HEDNet alone. In the future we want to evaluate if this framework is able to improve the performance in combination with other segmentation models.
```

### 人工综合要点

- 研究问题：见后续 `key_paper_analysis.md` 的人工归纳表。
- 方法、数据集、指标、优势、不足和可借鉴点：在后续综合表中统一给出，避免仅凭 PDF 自动抽取片段下结论。

## P28 SAT-Net: Structure-Aware Transformer-Based Attention Fusion Network for Low-Quality Retinal FunduImages Enhancement

- 选择理由：SAT-Net，代表低质量眼底图像增强和结构感知增强，可对接低质量感知增强模块。
- 本地文件：`眼底视网膜病变分割-论文PDF/眼底视网膜病变分割/2025-TMM-SAT-Net_Structure-Aware_Transformer-Based_Attention_Fusion_Network_for_Low-Quality_Retinal_FunduImages_Enhancement.pdf`
- 类别/方向：眼底视网膜病变分割 / 低质量眼底图像增强
- 年份与标识：2025；DOI:10.1109/TMM.2025.3565935
- 自动抽取数据集线索：DRIVE
- 自动抽取损失/训练线索：adversarial loss
- 方法关键词：CLAHE; DECODER; Knowledge Distillation; Knowledge distillation; STRUCTURE-AWARE; Self-Attention; Structure-Aware; Structure-aware; TRANSFORMER; Transformer; decoder; distillation; encoder; knowledge distillation; self-attention; structure-aware; transformer

### 结构化阅读线索

**abstract**

```text
Abstract—In ophthalmology diagnosis, high-ﬁdelity fundus images are essential for disease diagnosis and intervention. However, many real-world clinical conditions may degrade the quality of the acquired images and thus affect clinical diagnostic accuracy. Traditional convolutional neural network-based retinal fundus image enhancement methods cannot always capture longrange dependencies, which reduces the overall visual quality of images, especially for real retinal fundus images. Furthermore, existing enhancement methods often fail to fully utilize lowresolution structural detail information, which potentially leads to inaccurate pivotal fundus vessel topology or capillary details. In this paper, we propose a novel Structure-Aware Transformerbased attention fusion Network (SAT-Net) for low-quality retinal fundus image enhancement. First, we introduce a Transformerbased attention fusion module which incorporates windowbased self-attention and channel self-attention to capture global spatial dependencies and emphasize important feature channels simultaneously. This fusion signiﬁcantly improves the overall perceptual quality of the image by enhancing both the local details and the uniformity of the non-vessel background regions. Second, we introduce a cross-quality knowledge distillation technique, which bridges the quality gap between high-quality and low-quality fundus images. By designing a high-performing teacher network to guide a lightweight student network, the student network enables to capture detailed features from low-quality fundus images, further preserving critic
```

**method**

```text
methods cannot always capture longrange dependencies, which reduces the overall visual quality of images, especially for real retinal fundus images. Furthermore, existing enhancement methods often fail to fully utilize lowresolution structural detail information, which potentially leads to inaccurate pivotal fundus vessel topology or capillary details. In this paper, we propose a novel Structure-Aware Transformerbased attention fusion Network (SAT-Net) for low-quality retinal fundus image enhancement. First, we introduce a Transformerbased attention fusion module which incorporates windowbased self-attention and channel self-attention to capture global spatial dependencies and emphasize important feature channels simultaneously. This fusion signiﬁcantly improves the overall perceptual quality of the image by enhancing both the local details and the uniformity of the non-vessel background regions. Second, we introduce a cross-quality knowledge distillation technique, which bridges the quality gap between high-quality and low-quality fundus images. By designing a high-performing teacher network to guide a lightweight student network, the student network enables to capture detailed features from low-quality fundus images, further preserving critical diagnostic information and ﬁne topology structures. Moreover, we design a structure-aware multiscale loss function by using a trainable subnetwork to obtain the edge structure from different scales to better constrain pivotal fundus vessel structure and capillary details. Comprehensive Received 14 August 2024; revised 10 November 2
```

**experiment**

```text
experiments on both synthetic and real fundus image datasets robustly validate that our proposed SAT- Net outperforms other state-of-the-art methods for fundus image enhancement. In addition, extensive comparative experiments on both the vessel segmentation and Optic Disc/Cup detection tasks further validate the effectiveness and superiority of our proposed method. Index Terms—Cross-quality knowledge distillation, fundus imageenhancement,structure-awaremulti-scaleloss,transformerbased attention fusion. I. INTRODUCTION DUE to its inherent safety and cost-effectiveness, fundus photography has become a typical clinical instrument for the diagnosis and close monitoring of many ocular diseases in ophthalmology [3]. It is paramount for the early detection and accurate diagnosisofdiseasessuchasglaucoma,diabeticretinopathy,and cataracts [4]. However, a study using data from the U.K. Biobank found that only 71.53% of the images were suitable for vascular morphometric analysis [5]. This issue was primarily attributed to suboptimal imagingenvironments, suchas motion-inducedblurring and artifacts. This challenge underscores the importance of developing innovative and efﬁcient fundus image enhancement techniques. In recent years, advancements in fundus image enhancement have signiﬁcantly beneﬁted from the progress in deep learning technology. Though traditional fundus image enhancement methods can effectively improve image quality to some extent, they often rely on statistical prior knowledge and lack sensitivity to retinal details and stability of clinical variations, such as spatial ﬁ
```

**conclusion**

```text
CONCLUSION In this paper, we propose a SAT-Net to enhance low-quality retinal fundus images. Firstly, we propose the Transformer-based attention fusion module by incorporating both window self-attention blocks and channel attention blocks to highlight the local details and the uniformity of the non-vessel background regions. Secondly, we creatively introduce the cross-quality knowledge distillation technique by designing a highly-performing teacher network to guide a lightweight student network to fully capture the abundant detail features from the low-quality fundus images. Furthermore, we innovatively propose a structure-aware multi-scale loss function by designing a trainable edge detection subnetwork to obtain the critical edge structure at different scales, so as to enhance the constraints on pivotal fundus vessel structure and capillary details. Extensive experiments on multiple real and synthetic fundus images robustly validate that our SAT-Net outperforms other advanced methods for fundus image enhancement. Besides, sufﬁcient contrast experiments on vessel segmentation, optic disc and cup detection tasks also further validate the efﬁciency and superiority of our SAT-Net. Despite the pleasing performance, our SAT-Net also faces some challenges when dealing with extremely low-resolution images and overexposed images that make it difﬁcult to capture vascular information. In the future, we will work on improving the model’s adaptability across different retinal image datasets and exploring more advanced techniques for enhancing retinal structures of extremely low-resolu
```

### 人工综合要点

- 研究问题：见后续 `key_paper_analysis.md` 的人工归纳表。
- 方法、数据集、指标、优势、不足和可借鉴点：在后续综合表中统一给出，避免仅凭 PDF 自动抽取片段下结论。

## P06 KD-SAM Efficient Knowledge Distillation of SAM for Medical Image Segmentation

- 选择理由：KD-SAM，代表医学 SAM 蒸馏和轻量化部署方向。
- 本地文件：`眼底视网膜病变分割-论文PDF/SAM模型蒸馏/2025_KD-SAM_Efficient_Knowledge_Distillation_of_SAM_for_Medical_Image_Segmentation_arXiv2501.16740.pdf`
- 类别/方向：SAM模型蒸馏 / SAM 轻量化 / 蒸馏
- 年份与标识：2025；arXiv:2501.16740
- 自动抽取数据集线索：Breast Ultrasound; Fetal Head Ultrasound; ISIC 2017; Kvasir-SEG; Kvasir-seg; breast ultrasound; fetal head ultrasound
- 自动抽取损失/训练线索：Dice Loss; MSE; Perceptual Loss; Perceptual loss; perceptual loss
- 方法关键词：Decoder; Encoder; KNOWLEDGE DISTILLATION; Knowledge Distillation; Knowledge distillation; Prompt; SAM; Transformer; decoder; distillation; encoder; knowledge distillation; prompt; sam

### 结构化阅读线索

**abstract**

```text
ABSTRACT The Segment Anything Model (SAM) has set a new standard in interactive image segmentation, offering robust performance across various tasks. However, its significant computational requirements limit its deployment in real-time or resource-constrained environments. To address these challenges, we propose a novel knowledge distillation approach, KD SAM, which incorporates both encoder and decoder optimization through a combination of Mean Squared Error (MSE) and Perceptual Loss. This dual-loss framework captures structural and semantic features, enabling the student model to maintain high segmentation accuracy while reducing computational complexity. Based on the model evaluation on datasets, including Kvasir-SEG, ISIC 2017, Fetal Head Ultrasound, and Breast Ultrasound, we demonstrate that KD SAM achieves comparable or superior performance to the baseline models, with significantly fewer parameters. KD SAM effectively balances segmentation accuracy and computational efficiency, making it well-suited for real-time medical image segmentation applications in resource-constrained environments. Index Terms— Segment Anything Model (SAM), Knowledge Distillation, Medical Imaging, Computational Efficiency 1.
```

**method**

```text
framework captures structural and semantic features, enabling the student model to maintain high segmentation accuracy while reducing computational complexity. Based on the model
```

**experiment**

```text
evaluation on datasets, including Kvasir-SEG, ISIC 2017, Fetal Head Ultrasound, and Breast Ultrasound, we demonstrate that KD SAM achieves comparable or superior performance to the baseline models, with significantly fewer parameters. KD SAM effectively balances segmentation accuracy and computational efficiency, making it well-suited for real-time medical image segmentation applications in resource-constrained environments. Index Terms— Segment Anything Model (SAM), Knowledge Distillation, Medical Imaging, Computational Efficiency 1. INTRODUCTION Interactive image segmentation has become a cornerstone in numerous applications, including medical imaging, autonomous driving, and augmented reality. The Segment Anything Model (SAM) [1] has established itself as a powerful tool in this domain, leveraging a Vision Transformer (ViT) [2] encoder and prompt-guided mask decoder to achieve high segmentation accuracy across diverse datasets. However, the significant computational demands of SAM hinder its deployment in real-time and resource-constrained environments, such as mobile devices and edge platforms. MobileSAM [3] addresses these limitations by replacing the ViT encoder with ViT-Tiny, significantly reducing the model size and inference time while maintaining competitive performance. Despite these advances, the segmentation quality, particularly for complex tasks such as medical imaging, is compromised due to the reduced capacity of the ViT-Tiny encoder. In this work, we propose a novel decoupled knowledge distillation approach that enhances both the encoder and decoder compon
```

**conclusion**

```text
未抽取到稳定片段。
```

### 人工综合要点

- 研究问题：见后续 `key_paper_analysis.md` 的人工归纳表。
- 方法、数据集、指标、优势、不足和可借鉴点：在后续综合表中统一给出，避免仅凭 PDF 自动抽取片段下结论。

## P01 EdgeSAM: Prompt-In-the-Loop Distillation for SAM

- 选择理由：EdgeSAM，代表 prompt-in-the-loop 蒸馏，可借鉴到眼底病灶交互式/自动提示蒸馏。
- 本地文件：`眼底视网膜病变分割-论文PDF/SAM模型蒸馏/2023_EdgeSAM_Prompt-In-the-Loop_Distillation_arXiv2312.06660.pdf`
- 类别/方向：SAM模型蒸馏 / SAM 轻量化 / 蒸馏
- 年份与标识：2023；arXiv:2312.06660
- 自动抽取数据集线索：COCO; LVIS; Lvis; SA-1B; coco
- 自动抽取损失/训练线索：Dice loss; Focal loss; MSE; focal loss
- 方法关键词：Decoder; Distillation; Encoder; Knowledge Distillation; Prompt; SAM; Sam; decoder; distillation; encoder; knowledge distillation; prompt; sam; transformer

### 结构化阅读线索

**abstract**

```text
Abstract This paper presents EdgeSAM, an accelerated variant of the Segment Anything Model (SAM), optimized for efficient execution on edge devices with minimal compromise in performance. Our approach involves distilling the original ViT-based SAM image encoder into a purely CNN-based architecture, better suited for edge devices. We carefully benchmark various distillation strategies and demonstrate that task-agnostic encoder distillation fails to capture the full knowledge embodied in SAM. To overcome this bottleneck, we include both the prompt encoder and mask decoder in the distillation process, with box and point prompts in the loop, so that the distilled model can accurately capture the intricate dynamics between user input and mask generation. To mitigate dataset bias issues stemming from point prompt distillation, we incorporate a lightweight module within the encoder. As a result, EdgeSAM achieves a 37-fold speed increase compared to the original SAM, and it also outperforms MobileSAM/EfficientSAM, being over 7 times as fast when deployed on edge devices while enhancing the mIoUs on COCO and LVIS by 2.3/1.5 and 3.1/1.6, respectively. It is also the first SAM variant that can run at over 30 FPS on an iPhone 14. Code and demo are available here. Chong Zhou S-Lab, Nanyang Technological University, Singapore E-mail: chong003@ntu.edu.sg Xiangtai Li S-Lab, Nanyang Technological University, Singapore E-mail: xiangtai.li@ntu.edu.sg Chen Change Loy Corresponding Author S-Lab, Nanyang Technological University, Singapore E-mail: ccloy@ntu.edu.sg Bo Dai The University of Hong K
```

**method**

```text
method that aligns marginally with the SAM principles. EfficientSAM (Xiong et al, 2023) has achieved a great speedperformance trade-off through masked image pre-training, but it consumes a huge computational cost during training, and as it uses the same image encoder as MobileSAM, it runs no faster than MobileSAM. Our work further explores the setting where both training and inference budgets are more limited. Recently, SAM 2 (Ravi et al, 2024) extends SAM to the video domain, and several works optimize SAM 2 for efficient inference (Xiong et al, 2024; Zhou et al, 2025). Our work can also contribute to the SAM pre-training stage for these methods. The design philosophy of the proposed prompt-in-the-loop knowledge distillation is also related to refinement-based dense prediction methods such as Cascade-RCNN Cai and Vasconcelos (2018) and Refine- Mask Zhang et al (2021), but with a focus on distillation instead of architecture. Efficient Segmentation Models. Prior studies in efficient segmentation (Zhao et al, 2018; Li et al, 2020; Yu et al, 2018; Hu et al, 2023; Hong et al, 2021a; Wan et al, 2023; Yu et al, 2021; Li et al, 2023; Mehta et al, 2019, 2018; Hong et al, 2021b) have predominantly concentrated on closeset segmentation within specific domains, with a significant portion of this research (Li et al, 2020; Hu et al, 2023; Mehta et al, 2019) specifically targeting driving scenarios. More recently, a few works (Zhang et al, 2022; Wan et al, 2023) have ventured into designing segmentation models suitable for on-device implementation, capable of running efficiently on mobi
```

**experiment**

```text
experimental section. Additionally, we conducted thorough ablation studies focusing on the selection of the backbone architecture, particularly in view of the throughput-performance balance crucial for on-device deployment. We find that purely CNNbased architectures emerge as the more advantageous choice to ViT-based backbones for achieving the optimal trade-off. This is attributed to the current landscape of on-device AI accelerators, such as Apple Neural Engine (ANE), which are predominantly optimized for CNNs rather than ViT architectures. This observation also underscores the versatility of our proposed prompt-aware knowledge distillation approach, highlighting its applicability across diverse architectures. In our final observations, we note that SAM, having been trained on a dataset with multi-grained annotations, encounters challenges in resolving the granularity of output when faced with ambiguous prompts, such as a single point. This is particularly evident when SAM is prompted with center points on the COCO dataset during evaluations; the model does not consistently produce instance-level masks, but rather part-level masks. This issue becomes more pronounced when SAM functions as the teacher model. To address this, we propose a simple yet effective module designed to explicitly discern and adapt to the granularity priors specific to a given test set or application scenario. This module enhances SAM’s ability to interpret and respond to varying levels of prompt ambiguity accurately. Consequently, our EdgeSAM model achieves a remarkable performance boost, operating 
```

**conclusion**

```text
discussions through comprehensive ablation studies. 3.2.3 Granularity Priors Since SA-1B is a class-agnostic, multi-grained, automatically labeled dataset, its annotation distribution can be very different from that of the datasets that are intensively labeled by human labor, such as COCO. Therefore, with ambiguous prompts, such as a single point, it is hard for SAM to determine the desired output granularity. Meanwhile, as shown in Fig. 2, with box prompts, SAM can easily pinpoint the target granularity. In addition, compared to iteratively clicking or interacting with the box, there are many circumstances and applications on smartphones that a single click is favored, such as click-and-drag. Therefore, we propose a simple and efficient module that explicitly embeds the granularity priors of certain datasets and can be optionally turned off if the original behavior of SAM is preferred. With the image encoder staying frozen, we build a lightweight region proposal network (RPN) (Ren et al, 2015) on top of it, which consists of a feature pyramid network (FPN) (Lin et al, 2017a) and a shared detection head. For efficiency, we follow the design proposed by Efficient- Det (Tan et al, 2020). The RPN is trained on a specific dataset, e.g., COCO (Lin et al, 2014), to capture its granularity prior. During inference, we merge the proposal boxes whose centers are K nearest neighbors of the point prompts weighted by their confidence scores. Finally, we combine the merged box with the point input together as the prompt that inputs to the mask decoder. 3.3 Training and Application Traini
```

### 人工综合要点

- 研究问题：见后续 `key_paper_analysis.md` 的人工归纳表。
- 方法、数据集、指标、优势、不足和可借鉴点：在后续综合表中统一给出，避免仅凭 PDF 自动抽取片段下结论。
