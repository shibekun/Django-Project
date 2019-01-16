# Generated by Django 2.1.4 on 2019-01-14 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deliveries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inning', models.IntegerField(blank=True, null=True)),
                ('batting_team', models.CharField(blank=True, max_length=100, null=True)),
                ('bowling_team', models.CharField(blank=True, max_length=100, null=True)),
                ('over', models.IntegerField(blank=True, null=True)),
                ('ball', models.IntegerField(blank=True, null=True)),
                ('batsman', models.CharField(blank=True, max_length=100, null=True)),
                ('non_striker', models.CharField(blank=True, max_length=100, null=True)),
                ('bowler', models.CharField(blank=True, max_length=100, null=True)),
                ('is_super_over', models.IntegerField(blank=True, null=True)),
                ('wide_runs', models.IntegerField(blank=True, null=True)),
                ('bye_runs', models.IntegerField(blank=True, null=True)),
                ('legbye_runs', models.IntegerField(blank=True, null=True)),
                ('noball_runs', models.IntegerField(blank=True, null=True)),
                ('penalty_runs', models.IntegerField(blank=True, null=True)),
                ('batsman_runs', models.IntegerField(blank=True, null=True)),
                ('extra_runs', models.IntegerField(blank=True, null=True)),
                ('total_runs', models.IntegerField(blank=True, null=True)),
                ('player_dismissed', models.CharField(blank=True, max_length=100, null=True)),
                ('dismissal_kind', models.CharField(blank=True, max_length=50, null=True)),
                ('fielder', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'deliveries',
            },
        ),
        migrations.CreateModel(
            name='Matches',
            fields=[
                ('ids', models.IntegerField(primary_key=True, serialize=False)),
                ('season', models.IntegerField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.CharField(blank=True, max_length=50, null=True)),
                ('team1', models.CharField(blank=True, max_length=100, null=True)),
                ('team2', models.CharField(blank=True, max_length=100, null=True)),
                ('toss_winner', models.CharField(blank=True, max_length=100, null=True)),
                ('toss_decision', models.CharField(blank=True, max_length=100, null=True)),
                ('result', models.CharField(blank=True, max_length=50, null=True)),
                ('dl_applied', models.IntegerField(blank=True, null=True)),
                ('winner', models.CharField(blank=True, max_length=100, null=True)),
                ('win_by_runs', models.IntegerField(blank=True, null=True)),
                ('win_by_wickets', models.IntegerField(blank=True, null=True)),
                ('player_of_match', models.CharField(blank=True, max_length=100, null=True)),
                ('venue', models.CharField(blank=True, max_length=200, null=True)),
                ('umpire1', models.CharField(blank=True, max_length=200, null=True)),
                ('umpire2', models.CharField(blank=True, max_length=200, null=True)),
                ('umpire3', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'matches',
            },
        ),
        migrations.AddField(
            model_name='deliveries',
            name='match_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='iplapi.Matches'),
        ),
    ]