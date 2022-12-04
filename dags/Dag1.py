from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
import img_tools

dag = DAG(
    "train_dag",
    start_date=days_ago(0, 0, 0, 0, 0)
)


# def xui():
#     transformations = transforms.Compose([
#         transforms.Resize(255),
#         transforms.CenterCrop(224),
#         transforms.ToTensor()
#     ])
#     original_dataset = datasets.ImageFolder(r'C:\Users\door\PycharmProjects\airflow_weather_recognition\data_1',
#                                             transform=transformations)  # Здесь должна быть наша папочка в яндекс облаке
#     og_trn_size = int(0.7 * len(original_dataset))
#     og_val_size = int(0.1 * len(original_dataset))
#     og_tst_size = len(original_dataset) - og_trn_size - og_val_size
#     import torch
#     train_ds, val_ds, test_ds = torch.utils.data.random_split(original_dataset, [og_trn_size, og_val_size, og_tst_size])
#
#     augment_train_ds1 = copy.deepcopy(train_ds)
#     augment_train_ds1.dataset.transform = transforms.Compose([transforms.Resize(255),
#                                                               transforms.RandomCrop(224),
#                                                               transforms.RandomHorizontalFlip(p=1),
#                                                               transforms.ToTensor()])
#     augment_train_ds2 = copy.deepcopy(train_ds)
#     augment_train_ds2.dataset.transform = transforms.Compose([transforms.Resize(255),
#                                                               transforms.RandomCrop(224),
#                                                               transforms.RandomHorizontalFlip(p=0.7),
#                                                               transforms.RandomRotation(20),
#                                                               transforms.ToTensor()])
#     augment_train_ds3 = copy.deepcopy(train_ds)
#     augment_train_ds3.dataset.transform = transforms.Compose([transforms.Resize(255),
#                                                               transforms.RandomCrop(224),
#                                                               transforms.RandomHorizontalFlip(p=0.7),
#                                                               transforms.RandomPerspective(distortion_scale=0.3, p=1),
#                                                               transforms.ToTensor()])
#
#     train_ds = torch.utils.data.ConcatDataset([train_ds, augment_train_ds1])
#     train_ds = torch.utils.data.ConcatDataset([train_ds, augment_train_ds2])
#     train_ds = torch.utils.data.ConcatDataset([train_ds, augment_train_ds3])


def read_dataset():
    data = img_tools.download_img()
    # zipPath = r'C:\Users\door\PycharmProjects\airflow_weather_recognition\data\xui.zip'
    zip_path = "xui.zip"
    # directory_to_extract_to = r'C:\Users\door\PycharmProjects\airflow_weather_recognition\data_1'
    directory_to_extract_to = "data_1"
    # zipPath = r'airflow_weather_recognition\data\xui.zip'
    with open(zip_path, 'wb') as zipFile:
        zipFile.write(data)
    print("2")
    import zipfile
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(directory_to_extract_to)
    print("3")


downdload_dataframe = PythonOperator(
    task_id='download_dataset',
    python_callable=read_dataset,
    dag=dag
)
#
# augmentation = PythonOperator(
#     task_id='dataset_augmentation',
#     python_callable=read_dataset,
#     dag=dag
# )
