_base_ = './htc_without_semantic_r50_fpn_1x_coco.py'
model = dict(
    roi_head=dict(
        semantic_roi_extractor=dict(
            type='SingleRoIExtractor',
            roi_layer=dict(type='RoIAlign', output_size=14, sampling_ratio=0),
            out_channels=256,
            featmap_strides=[8]),
        semantic_head=dict(
            type='FusedSemanticHead',
            num_ins=5,
            fusion_level=1,
            num_convs=4,
            in_channels=256,
            conv_out_channels=256,
            num_classes=183,
            loss_seg=dict(
                type='CrossEntropyLoss', ignore_index=255, loss_weight=0.2))))
data_root = 'data/coco/'
img_norm_cfg = dict(
    mean=[123.675, 116.28, 103.53], std=[58.395, 57.12, 57.375], to_rgb=True)
train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(
        type='LoadAnnotations', with_bbox=True, with_mask=True, with_seg=True),
    dict(type='Resize', img_scale=(1333, 800), keep_ratio=True),
    dict(type='RandomFlip', flip_ratio=0.5),
    dict(type='Normalize', **img_norm_cfg),
    dict(type='Pad', size_divisor=32),
    dict(type='SegRescale', scale_factor=1 / 8),
    dict(type='DefaultFormatBundle'),
    dict(
        type='Collect',
        keys=['img', 'gt_bboxes', 'gt_labels', 'gt_masks', 'gt_semantic_seg']),
]
test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(
        type='MultiScaleFlipAug',
        img_scale=(1333, 800),
        flip=False,
        transforms=[
            dict(type='Resize', keep_ratio=True),
            dict(type='RandomFlip', flip_ratio=0.5),
            dict(type='Normalize', **img_norm_cfg),
            dict(type='Pad', size_divisor=32),
            dict(type='ImageToTensor', keys=['img']),
            dict(type='Collect', keys=['img']),
        ])
]
# data = dict(
#     train=dict(
#         seg_prefix=data_root + 'stuffthingmaps/train2017/',
#         pipeline=train_pipeline),
#     val=dict(pipeline=test_pipeline),
#     test=dict(pipeline=test_pipeline))
dataset_type = 'CocoDataset'
classes = ("Nóc xe ","Viền nóc (mui)","Pa vô lê","Kính chắn gió trước","Ca pô trước","Ca lăng","Lưới ca lăng","Ba đờ sốc trước","Lưới ba đờ sốc","Ốp ba đờ sốc trước","Lô gô","Đèn phản quang ba đờ sốc sau","Cốp sau / Cửa hậu","Ba đờ sốc sau","Ốp ba đờ sốc sau","Kính chắn gió sau","Đèn gầm","Ốp đèn  gầm","Cụm đèn trước","Mặt gương (kính) chiếu hậu","Vỏ gương (kính) chiếu hậu","Chân gương (kính) chiếu hậu","Đèn xi nhan trên gương chiếu hậu","Trụ kính trước","Tai (vè trước) xe","Ốp Tai (vè trước) xe","Đèn xi nhan ba đ sốc","Ốp đèn xi nhan ba đ sốc","Đèn hậu","Kính chết góc cửa","Kính hông (xe 7 chỗ)","Hông (vè sau) xe","Trụ kính sau","Đèn hậu trên cốp sau","La giăng (Mâm xe)","Lốp (vỏ) xe","Tay mở cửa","Kính cánh cửa","Cánh cửa","Móp, bẹp(thụng)","Nứt, rạn","Vỡ, thủng, rách","Trầy, xước","Trụ kính cánh cửa","Ốp hông (vè sau) xe","Nẹp cốp sau","Bậc cánh cửa","Nẹp ca pô trước",)
data = dict(
    samples_per_gpu=2,
    workers_per_gpu=2,
    train=dict(
        type=dataset_type,
        ann_file= '/home/a4000/huyenhc/Swin-Transformer-Object-Detection/dataset/data_2305/dataset_train.json',
        classes = classes,
        img_prefix= "/home/a4000/huyenhc/Swin-Transformer-Object-Detection/dataset/data_2305/data_remove_text",
        pipeline=train_pipeline),
    val=dict(
        type=dataset_type,
        ann_file='/home/a4000/huyenhc/Swin-Transformer-Object-Detection/dataset/data_2305/dataset_test.json',
        img_prefix='/home/a4000/huyenhc/Swin-Transformer-Object-Detection/dataset/data_2305/data_remove_text',
        pipeline=test_pipeline,
        classes = classes,),
    test=dict(
        type=dataset_type,
        ann_file='/home/a4000/huyenhc/Swin-Transformer-Object-Detection/dataset/data_2305/dataset_test.json',
        img_prefix='/home/a4000/huyenhc/Swin-Transformer-Object-Detection/dataset/data_2305/data_remove_text',
        pipeline=test_pipeline,
        classes = classes,))
