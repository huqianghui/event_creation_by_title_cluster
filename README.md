# event_creation_by_title_cluster

## 1。把新闻标题向量化

<img width="933" alt="Screenshot 2023-08-18 at 16 57 33" src="https://github.com/huqianghui/event_creation_by_title_cluster/assets/7360524/3c428e11-fdd7-4e1b-8e7c-116ebeb01d93">

## 2. 把向量的1538维度作为计算特征

<img width="1153" alt="Screenshot 2023-08-18 at 16 55 59" src="https://github.com/huqianghui/event_creation_by_title_cluster/assets/7360524/7a1dbe79-a1b4-4b8b-9b1d-302cf8233cda">

## 3. 计算特征之间的余弦值作为标尺

<img width="1125" alt="Screenshot 2023-08-18 at 16 55 07" src="https://github.com/huqianghui/event_creation_by_title_cluster/assets/7360524/21d32436-3400-4317-a480-dad1308dcc6f">

## 4. 通过余弦值计算，或者 OPTICS算法等，得到非监督学习的簇集

<img width="1660" alt="optics" src="https://github.com/huqianghui/event_creation_by_title_cluster/assets/7360524/1493d88e-cf03-4f96-bbf2-fc67150177e0">

## 5. 通过gpt4，对这些簇集的的标题作为输入，总结出热点事件内容

<img width="1193" alt="Screenshot 2023-08-18 at 16 53 19" src="https://github.com/huqianghui/event_creation_by_title_cluster/assets/7360524/f4a3e956-55a4-4810-890d-5bacefe130ca">

