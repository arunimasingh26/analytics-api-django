from .models import Dataset

def save_dataset(file_name, summary):
    Dataset.objects.create(
        file_name=file_name,
        summary=summary
    )
    cleanup_old_datasets()

def get_recent_datasets():
    return Dataset.objects.order_by('-uploaded_at')

def cleanup_old_datasets():
    datasets = get_recent_datasets()
    if datasets.count() > 5:
        for ds in datasets[5:]:
            ds.delete()
