# Generated by Django 3.0.3 on 2020-03-20 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('trading_post', '0002_auto_20200319_2044'),
    ]

    operations = [
        migrations.AddField(
            model_name='deck',
            name='hand',
            field=models.ManyToManyField(related_name='deck_hand_cards', to='trading_post.Card'),
        ),
        migrations.AlterField(
            model_name='deck',
            name='cards',
            field=models.ManyToManyField(related_name='deck_cards', to='trading_post.Card'),
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initiator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='initiator', to='accounts.Profile')),
                ('initiator_deck', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='initiator_deck', to='accounts.Profile')),
                ('other_deck', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='other_deck', to='accounts.Profile')),
                ('other_player', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='other_player', to='accounts.Profile')),
            ],
        ),
    ]
