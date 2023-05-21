# Generated by Django 4.0.2 on 2022-02-20 16:35

import django.contrib.gis.db.models.fields
import django.db.models.deletion
import modelcluster.fields
from django.db import migrations, models
import wagtail.blocks as wagtail_blocks
import wagtail.fields as wagtail_fields

import wagtailgeowidget.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("wagtailcore", "0066_collection_management_permissions"),
    ]

    streamfield_params = {"use_json_field": True}

    operations = [
        migrations.CreateModel(
            name="ClassicGeoPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                ("address", models.CharField(blank=True, max_length=250, null=True)),
                ("location", models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="ClassicGeoPageWithLeaflet",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "address",
                    models.CharField(
                        blank=True,
                        help_text="Search powered by MapBox",
                        max_length=250,
                        null=True,
                    ),
                ),
                ("location", models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="ClassicGeoPageWithLeafletAndZoom",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "address",
                    models.CharField(
                        blank=True,
                        help_text="Search powered by Nominatim",
                        max_length=250,
                        null=True,
                    ),
                ),
                ("location", models.CharField(blank=True, max_length=250, null=True)),
                ("zoom", models.SmallIntegerField(blank=True, null=True)),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="ClassicGeoPageWithZoom",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                ("address", models.CharField(blank=True, max_length=250, null=True)),
                ("location", models.CharField(blank=True, max_length=250, null=True)),
                ("zoom", models.SmallIntegerField(blank=True, null=True)),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="GeoLocation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("address", models.CharField(blank=True, max_length=250, null=True)),
                ("zoom", models.SmallIntegerField(blank=True, null=True)),
                (
                    "location",
                    django.contrib.gis.db.models.fields.PointField(
                        blank=True, null=True, srid=4326
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="GeoLocationWithLeaflet",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                (
                    "address",
                    models.CharField(
                        blank=True,
                        help_text="Search powered by Nominatim",
                        max_length=250,
                        null=True,
                    ),
                ),
                ("zoom", models.SmallIntegerField(blank=True, null=True)),
                (
                    "location",
                    django.contrib.gis.db.models.fields.PointField(
                        blank=True, null=True, srid=4326
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="GeoPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                ("address", models.CharField(blank=True, max_length=250, null=True)),
                (
                    "location",
                    django.contrib.gis.db.models.fields.PointField(
                        blank=True, null=True, srid=4326
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="GeoPageWithLeaflet",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "address",
                    models.CharField(
                        blank=True,
                        help_text="Search powered by Nominatim",
                        max_length=250,
                        null=True,
                    ),
                ),
                (
                    "location",
                    django.contrib.gis.db.models.fields.PointField(
                        blank=True, null=True, srid=4326
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="GeoStreamPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "body",
                    wagtail_fields.StreamField(
                        [
                            ("map", wagtailgeowidget.blocks.GoogleMapsBlock()),
                            (
                                "map_with_leaflet",
                                wagtailgeowidget.blocks.LeafletBlock(),
                            ),
                            (
                                "map_struct",
                                wagtail_blocks.StructBlock(
                                    [
                                        (
                                            "address",
                                            wagtailgeowidget.blocks.GeoAddressBlock(
                                                required=True
                                            ),
                                        ),
                                        (
                                            "map",
                                            wagtailgeowidget.blocks.GoogleMapsBlock(
                                                address_field="address"
                                            ),
                                        ),
                                    ],
                                    icon="user",
                                ),
                            ),
                            (
                                "map_struct_with_deprecated_geopanel",
                                wagtail_blocks.StructBlock(
                                    [
                                        (
                                            "address",
                                            wagtail_blocks.CharBlock(required=True),
                                        ),
                                        (
                                            "map",
                                            wagtailgeowidget.blocks.GeoBlock(
                                                address_field="address"
                                            ),
                                        ),
                                    ],
                                    icon="user",
                                ),
                            ),
                            (
                                "map_struct_with_leaflet",
                                wagtail_blocks.StructBlock(
                                    [
                                        (
                                            "address",
                                            wagtailgeowidget.blocks.GeoAddressBlock(
                                                required=True
                                            ),
                                        ),
                                        (
                                            "map",
                                            wagtailgeowidget.blocks.LeafletBlock(
                                                address_field="address"
                                            ),
                                        ),
                                    ],
                                    icon="user",
                                ),
                            ),
                            (
                                "map_struct_with_zoom",
                                wagtail_blocks.StructBlock(
                                    [
                                        (
                                            "address",
                                            wagtailgeowidget.blocks.GeoAddressBlock(
                                                required=True
                                            ),
                                        ),
                                        (
                                            "zoom",
                                            wagtailgeowidget.blocks.GeoZoomBlock(
                                                required=False
                                            ),
                                        ),
                                        (
                                            "map",
                                            wagtailgeowidget.blocks.GoogleMapsBlock(
                                                address_field="address",
                                                zoom_field="zoom",
                                            ),
                                        ),
                                    ],
                                    icon="user",
                                ),
                            ),
                            (
                                "map_struct_leaflet_with_zoom",
                                wagtail_blocks.StructBlock(
                                    [
                                        (
                                            "address",
                                            wagtailgeowidget.blocks.GeoAddressBlock(
                                                required=True
                                            ),
                                        ),
                                        (
                                            "zoom",
                                            wagtailgeowidget.blocks.GeoZoomBlock(
                                                required=False
                                            ),
                                        ),
                                        (
                                            "map",
                                            wagtailgeowidget.blocks.LeafletBlock(
                                                address_field="address",
                                                zoom_field="zoom",
                                            ),
                                        ),
                                    ],
                                    icon="user",
                                ),
                            ),
                        ],
                        **streamfield_params,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="GeoPageWithLeafletRelatedLocations",
            fields=[
                (
                    "geolocationwithleaflet_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="geopage.geolocationwithleaflet",
                    ),
                ),
                (
                    "sort_order",
                    models.IntegerField(blank=True, editable=False, null=True),
                ),
                (
                    "page",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="related_locations",
                        to="geopage.geopagewithleaflet",
                    ),
                ),
            ],
            options={
                "ordering": ["sort_order"],
                "abstract": False,
            },
            bases=("geopage.geolocationwithleaflet", models.Model),
        ),
        migrations.CreateModel(
            name="GeoPageRelatedLocations",
            fields=[
                (
                    "geolocation_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="geopage.geolocation",
                    ),
                ),
                (
                    "sort_order",
                    models.IntegerField(blank=True, editable=False, null=True),
                ),
                (
                    "page",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="related_locations",
                        to="geopage.geopage",
                    ),
                ),
            ],
            options={
                "ordering": ["sort_order"],
                "abstract": False,
            },
            bases=("geopage.geolocation", models.Model),
        ),
    ]
