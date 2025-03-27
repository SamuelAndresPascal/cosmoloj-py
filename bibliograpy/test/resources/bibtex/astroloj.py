from bibliograpy.api_bibtex import *


NASA = Misc.generic(cite_key='nasa',
                    institution='NASA',
                    title='NASA')

IAU = Misc.generic(cite_key='iau',
                   institution='IAU',
                   title='International Astronomical Union')

WMO = Misc.generic(cite_key='wmo',
                   institution='WMO',
                   title='World Meteorological Organization')

IERS = Misc.generic(cite_key='iers',
                    institution='IERS',
                    title='International Earth rotation and Reference systems Service')

OBSPM = Misc.generic(cite_key='obspm',
                     title='Observatoire de Paris',
                     non_standard=NonStandard(url='https://www.obspm.fr/'))

IMCCE = Misc.generic(cite_key='imcce',
                     title='Institut de Mécanique Céleste et de Calcul des Éphémérides',
                     non_standard=NonStandard(url='https://www.imcce.fr/'))

OGC = Misc.generic(cite_key='ogc',
                   institution='OGC',
                   title='Open Geospatial Consortium')

ISO = Misc.generic(cite_key='iso',
                   title='ISO')

W3C = Misc.generic(cite_key='w3c',
                   institution='W3C',
                   title='World Wide Web Consortium')

UCAR = Misc.generic(cite_key='ucar',
                    institution='UCAR',
                    title='University Corporation for Atmospheric Research')

ASTRONOMY_ASTROPHYSICS = Misc.generic(cite_key='astronomy_astrophysics',
                                      journal='A&A',
                                      title='Astronomy & Astrophysics',
                                      non_standard=NonStandard(issn='0004-6361', url='https://www.aanda.org/'))

ASTRONOMY_ASTROPHYSICS_SUPPL_SERIES = Misc.generic(cite_key='astronomy_astrophysics_suppl_series',
                                                   journal='Astronomy and Astrophysics supplement series',
                                                   title='Astronomy and Astrophysics supplement series',
                                                   non_standard=NonStandard(issn='0365-0138', url='https://aas.aanda.org/'))

BULLETIN_ASTRONOMIQUE = Misc.generic(cite_key='bulletin_astronomique',
                                     title='Bulletin astronomique')

THE_ASTRONOMICAL_JOURNAL = Misc.generic(cite_key='the_astronomical_journal',
                                        journal='The Astronomical Journal',
                                        title='The Astronomical Journal')

ASTRONOMY_GEOPHYSICS = Misc.generic(cite_key='astronomy_geophysics',
                                    journal='Astronomy & Geophysics',
                                    title='Astronomy & Geophysics')

CELESTIAL_MECHANICS = Misc.generic(cite_key='celestial_mechanics',
                                   journal='Celestial Mechanics',
                                   title='Celestial Mechanics')

CELESTIAL_MECHANICS_DYNAMICAL_ASTRONOMY = Misc.generic(cite_key='celestial_mechanics_dynamical_astronomy',
                                                       title='Celestial Mechanics & Dynamical Astronomy',
                                                       non_standard=NonStandard(issn='0923-2958'))

JOURNAL_GEOPHYSICAL_RESEARCH = Misc.generic(cite_key='journal_geophysical_research',
                                            journal='Journal of Geophysical Research',
                                            title='Journal of Geophysical Research',
                                            non_standard=NonStandard(issn='0148-0227'))

JOURNAL_HISTORY_ASTRONOMY = Misc.generic(cite_key='journal_history_astronomy',
                                         journal='Journal for the History of Astronomy',
                                         title='Journal for the History of Astronomy',
                                         non_standard=NonStandard(issn='0021-8286'))

ASTRONOMICAL_ALMANAC = Misc.generic(cite_key='astronomical_almanac',
                                    title='The Astronomical Almanac')

INTERNATIONAL_ASTRONOMICAL_UNION_COLLOQUIUM = Proceedings.generic(cite_key='international_astronomical_union_colloquium',
                                                                  booktitle='International Astronomical Union Colloquium',
                                                                  title='International Astronomical Union Colloquium',
                                                                  year=2000,
                                                                  non_standard=NonStandard(issn='0252-9211'))

CELESTIAL_MECHANICS_AND_DYNAMICAL_ASTRONOMY = Misc.generic(cite_key='celestial_mechanics_and_dynamical_astronomy',
                                                           journal='Celestial Mechanics & Dynamical Astronomy',
                                                           title='Celestial Mechanics & Dynamical Astronomy',
                                                           non_standard=NonStandard(issn='0923-2958'))

ASTRONOMICAL_ALMANAC_1997 = Book.generic(cite_key='astronomical_almanac_1997',
                                         author='Defense Dept., Navy, Nautical Almanac Office',
                                         crossref=ASTRONOMICAL_ALMANAC,
                                         editor='U.S. Government Printing Office',
                                         publisher='',
                                         title='The Astronomical Almanac for the year 1997',
                                         year=1996)

STEPHENSON_1997 = Book.generic(cite_key='stephenson_1997',
                               editor='Cambridge University Press',
                               publisher='',
                               title="Historical Eclipses and Earth's Rotation",
                               year=1997)

ASTRONOMICAL_ALMANAC_2013 = Book.generic(cite_key='astronomical_almanac_2013',
                                         author='Defense Dept., Navy, Nautical Almanac Office',
                                         crossref=ASTRONOMICAL_ALMANAC,
                                         editor='U.S. Government Printing Office',
                                         publisher='',
                                         title='The Astronomical Almanac for the year 2013',
                                         year=2012,
                                         non_standard=NonStandard(url='https://books.google.fr/books?id=7fl_-DLwJ8YC&lpg=PP1&dq=the%20astronomical%20almanac&hl=fr&pg=PP1#v=onepage&q=the%20astronomical%20almanac&f=false'))

ASTRONOMICAL_ALMANAC_2017 = Book.generic(cite_key='astronomical_almanac_2017',
                                         author='Defense Department, The Stationery Office, U S Nautical Almanac Office',
                                         crossref=ASTRONOMICAL_ALMANAC,
                                         editor='U.S. Government Printing Office',
                                         publisher='',
                                         title='The Astronomical Almanac for the year 2017',
                                         year=2016,
                                         non_standard=NonStandard(url='https://books.google.fr/books?id=5E9R8trNQ88C&lpg=SL14-PA2&dq=astronomical%20almanac%20k11&hl=fr&pg=PR2#v=onepage&q=astronomical%20almanac%20k11&f=false'))

CONNAISSANCE_DES_TEMPS_2015 = Book.generic(cite_key='connaissance_des_temps_2015',
                                           author='Bureau des Longitudes',
                                           editor='Gauthier-Villars',
                                           publisher='',
                                           title='Éphémérides astronomiques - Connaissance des temps',
                                           year=2015)

SIMON_AL_2013 = Article.generic(cite_key='simon_al_2013',
                                author='',
                                crossref=ASTRONOMY_ASTROPHYSICS,
                                title='New analytical planetary theories VSOP2013 and TOP2013',
                                volume='557',
                                year=2013,
                                non_standard=NonStandard(url='https://www.aanda.org/articles/aa/abs/2013/09/aa21843-13/aa21843-13.html'))

VONDRAK_AL_2011 = Article.generic(cite_key='vondrak_al_2011',
                                  author='',
                                  crossref=ASTRONOMY_ASTROPHYSICS,
                                  title='New precession expressions, valid for long-time intervals',
                                  volume='534',
                                  year=2011,
                                  non_standard=NonStandard(url='https://www.aanda.org/articles/aa/pdf/2011/10/aa17274-11.pdf'))

ORBITAL_EPHEMERIDES = Misc.generic(cite_key='orbital_ephemerides',
                                   note='Chapitre 8, par E. Myles Standish and James G. Williams.',
                                   title='Orbital Ephemerides of the Sun, Moon, and Planets',
                                   non_standard=NonStandard(url='ftp://ssd.jpl.nasa.gov/pub/eph/planets/ioms/ExplSupplChap8.pdf'))

ASTRONOMICAL_ALMANAC_ONLINE = Misc.generic(cite_key='astronomical_almanac_online',
                                           title='The Astronomical Almanac online',
                                           non_standard=NonStandard(url='http://asa.usno.navy.mil/'))

LASKAR_1984 = Phdthesis.generic(cite_key='laskar_1984',
                                author='',
                                school='',
                                title='Théorie Générale Planétaire. Eléments orbitaux des planètes sur 1 million d’années',
                                year=1984)

ESPENAK_MEEUS_2006 = TechReport.generic(cite_key='espenak_meeus_2006',
                                        author='',
                                        crossref=NASA,
                                        number='NASA/TP–2006–214141',
                                        title='Five Millennium Canon of Solar Eclipses: –1999 to +3000 (2000 BCE to 3000 CE)',
                                        type='document',
                                        year=2006,
                                        non_standard=NonStandard(url='https://eclipse.gsfc.nasa.gov/5MCSE/5MCSE-Text11.pdf'))

KOZAI_1973 = TechReport.generic(cite_key='kozai_1973',
                                author='',
                                crossref=NASA,
                                number='N73-17709',
                                title='A new method to compute lunisolar perturbations in satellite motions',
                                type='report',
                                year=1973,
                                non_standard=NonStandard(url='https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/19730008982.pdf'))

LIEZKE_1967 = TechReport.generic(cite_key='liezke_1967',
                                 author='',
                                 crossref=NASA,
                                 number='32-1044',
                                 title='Expressions for the Precession Quantities and Their Partial Derivatives',
                                 type='report',
                                 year=1967,
                                 non_standard=NonStandard(url='https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/19670020103.pdf'))

ANDOYER_1911 = Article.generic(cite_key='andoyer_1911',
                               author='',
                               crossref=ASTRONOMY_ASTROPHYSICS,
                               pages='67-76',
                               title="Les formules de la précession d'après S. Newcomb",
                               volume='28',
                               year=1911,
                               non_standard=NonStandard(url='https://www.aanda.org/articles/aa/abs/2013/09/aa21843-13/aa21843-13.html'))

BRETAGNON_1974_AA30 = Article.generic(cite_key='bretagnon_1974_aa30',
                                      author='',
                                      crossref=ASTRONOMY_ASTROPHYSICS,
                                      pages='141-154',
                                      title='Long-period terms in the solar system',
                                      volume='30',
                                      year=1974,
                                      non_standard=NonStandard(url='http://adsabs.harvard.edu/abs/1974A%26A....30..141B'))

CHAPRON_AL_1975 = Article.generic(cite_key='chapron_al_1975',
                                  author='',
                                  crossref=CELESTIAL_MECHANICS,
                                  pages='379-399',
                                  title='A formula for calculating higher-order perturbations in planetary problems',
                                  volume='11',
                                  year=1975,
                                  non_standard=NonStandard(url='http://adsabs.harvard.edu/abs/1975CeMec..11..379C'))

LIESKE_AL_1977 = Article.generic(cite_key='lieske_al_1977',
                                 author='',
                                 crossref=ASTRONOMY_ASTROPHYSICS,
                                 pages='1-16',
                                 title='Expressions for the Precession Quantities Based upon the IAU (1976) System of Astronomical Constants',
                                 volume='58',
                                 year=1977,
                                 non_standard=NonStandard(url='http://adsabs.harvard.edu/full/1977A%26A....58....1L'))

BRETAGNON_CHAPRONT_1981 = Article.generic(cite_key='bretagnon_chapront_1981',
                                          author='',
                                          crossref=ASTRONOMY_ASTROPHYSICS,
                                          pages='103-107',
                                          title='A note on the numerical expressions for precession calculations',
                                          volume='103',
                                          year=1981,
                                          non_standard=NonStandard(url='http://adsabs.harvard.edu/abs/1982A%26A...114..278B'))

LESTRADE_BRETAGNON_1982 = Article.generic(cite_key='lestrade_bretagnon_1982',
                                          author='',
                                          crossref=ASTRONOMY_ASTROPHYSICS,
                                          pages='42-52',
                                          title='Relativistic perturbations for all the planets',
                                          volume='105',
                                          year=1982,
                                          non_standard=NonStandard(url='http://adsabs.harvard.edu/abs/1982A%26A...105...42L'))

BRETAGNON_1982_AA108 = Article.generic(cite_key='bretagnon_1982_aa108',
                                       author='',
                                       crossref=ASTRONOMY_ASTROPHYSICS,
                                       pages='69-75',
                                       title='Integration constants and mean elements for the planetary system',
                                       volume='108',
                                       year=1982,
                                       non_standard=NonStandard(url='http://adsabs.harvard.edu/abs/1982A%26A...108...69B'))

BRETAGNON_1982 = Article.generic(cite_key='bretagnon_1982',
                                 author='',
                                 crossref=ASTRONOMY_ASTROPHYSICS,
                                 pages='278-288',
                                 title='Theory for the motion of all the planets - The VSOP82 solution',
                                 volume='114',
                                 year=1982,
                                 non_standard=NonStandard(url='http://adsabs.harvard.edu/abs/1982A%26A...114..278B'))

CHAPRONT_TOUZE_CHAPRONT_1983 = Article.generic(cite_key='chapront_touze_chapront_1983',
                                               author='',
                                               crossref=ASTRONOMY_ASTROPHYSICS,
                                               pages='50-62',
                                               title='The lunar ephemeris EPL 2000',
                                               volume='124',
                                               year=1983,
                                               non_standard=NonStandard(url='http://adsabs.harvard.edu/full/1983A%26A...124...50C'))

LASKAR_1985 = Article.generic(cite_key='laskar_1985',
                              author='',
                              crossref=ASTRONOMY_ASTROPHYSICS,
                              pages='133-146',
                              title='Accurate methods in general planetary theory',
                              volume='144',
                              year=1985,
                              non_standard=NonStandard(url='http://adsabs.harvard.edu/abs/1985A%26A...144..133L'))

LASKAR_1986 = Article.generic(cite_key='laskar_1986',
                              author='',
                              crossref=ASTRONOMY_ASTROPHYSICS,
                              pages='59-70',
                              title='Secular terms of classical planetary theories using the results of general theory',
                              volume='157',
                              year=1986,
                              non_standard=NonStandard(url='http://adsabs.harvard.edu/abs/1986A%26A...157...59L'))

BRETAGNON_FRANCOU_1988 = Article.generic(cite_key='bretagnon_francou_1988',
                                         author='',
                                         crossref=ASTRONOMY_ASTROPHYSICS,
                                         pages='309-315',
                                         title='Planetary theories in rectangular and spherical variables. VSOP87 solutions',
                                         volume='202',
                                         year=1988,
                                         non_standard=NonStandard(url='http://adsabs.harvard.edu/abs/1988A&A...202..309B'))

CAPITAINE_AL_2000 = Article.generic(cite_key='capitaine_al_2000',
                                    author='',
                                    crossref=ASTRONOMY_ASTROPHYSICS,
                                    pages='398-405',
                                    title='Definition of the Celestial Ephemeris Origin and of UT1 in the International Celestial Reference Frame',
                                    volume='355',
                                    year=2000,
                                    non_standard=NonStandard(url='http://articles.adsabs.harvard.edu/pdf/2000A%26A...355..398C'))

CAPITAINE_2000 = Inproceedings.generic(cite_key='capitaine_2000',
                                       author='',
                                       crossref=INTERNATIONAL_ASTRONOMICAL_UNION_COLLOQUIUM,
                                       pages='153-163',
                                       title='Definition of the Celestial Ephemeris Pole and the Celestial Ephemeris Origin',
                                       volume='182',
                                       year=2000,
                                       non_standard=NonStandard(url='https://www.cambridge.org/core/journals/international-astronomical-union-colloquium/article/definition-of-the-celestial-ephemeris-pole-and-the-celestial-ephemeris-origin/3ED19E4A0C612E8027D4256DA858255B'))

CAPITAINE_AL_1986 = Article.generic(cite_key='capitaine_al_1986',
                                    author='',
                                    crossref=CELESTIAL_MECHANICS,
                                    number='3',
                                    pages='283-307',
                                    title='A non-rotating origin on the instantaneous equator - Definition, properties and use',
                                    volume='39',
                                    year=1986,
                                    non_standard=NonStandard(url='http://articles.adsabs.harvard.edu//full/1986CeMec..39..283C'))

KINOSHITA_SOUCHAY_1990 = Article.generic(cite_key='kinoshita_souchay_1990',
                                         author='',
                                         crossref=CELESTIAL_MECHANICS_AND_DYNAMICAL_ASTRONOMY,
                                         month='september',
                                         pages='187-265',
                                         title='The Theory of the Nutation for the Rigid Earth Model at the Second Order',
                                         volume='48',
                                         year=1990,
                                         non_standard=NonStandard(url='https://ui.adsabs.harvard.edu/abs/1990CeMDA..48..187K/abstract'))

BRETAGNON_FRANCOU_1992 = Inproceedings.generic(cite_key='bretagnon_francou_1992',
                                               author='',
                                               booktitle='proceedings of the 152nd Symposium of the International Astronomical Union held in Angra dos Reis, Brazil, 15-19 July, 1991',
                                               title='General Theory for the Outer Planets',
                                               volume='152',
                                               year=1992)

MORRISON_STEPHENSON_2004 = Article.generic(cite_key='morrison_stephenson_2004',
                                           author='',
                                           crossref=JOURNAL_HISTORY_ASTRONOMY,
                                           note='part 3',
                                           number='120',
                                           pages='327-336',
                                           title="Historical values of the Earth's clock error ΔT and the calculation of eclipses",
                                           volume='35',
                                           year=1992,
                                           non_standard=NonStandard(url='http://articles.adsabs.harvard.edu/full/2004JHA....35..327M'))

STEPHENSON_2003 = Article.generic(cite_key='stephenson_2003',
                                  author='',
                                  crossref=ASTRONOMY_GEOPHYSICS,
                                  title="Historical Eclipses and Earth's Rotation",
                                  volume='44',
                                  year=2003,
                                  non_standard=NonStandard(url='http://astrogeo.oxfordjournals.org/content/44/2/2.22.full'))

WILLIAMS_AL_1994 = Article.generic(cite_key='williams_al_1994',
                                   author='',
                                   crossref=THE_ASTRONOMICAL_JOURNAL,
                                   number='2',
                                   pages='711-724',
                                   title="Contributions to the Earth's obliquity rate, precession, and nutation",
                                   volume='108',
                                   year=1994,
                                   non_standard=NonStandard(url='https://www.researchgate.net/publication/4687246_Contributions_to_the_Earth%27s_Obliquity_Rate_Precession_and_Nutation'))

SYRTE_OBSPM_FR_FTP = Misc.generic(cite_key='syrte_obspm_fr_ftp',
                                  crossref=OBSPM,
                                  non_standard=NonStandard(url='ftp://syrte.obspm.fr/'))

IMCCE_FR_FTP = Misc.generic(cite_key='imcce_fr_ftp',
                            crossref=IMCCE,
                            non_standard=NonStandard(url='ftp://ftp.imcce.fr/'))

HPIERS_OBSPM_FR_HTTP = Misc.generic(cite_key='hpiers_obspm_fr_http',
                                    crossref=OBSPM,
                                    non_standard=NonStandard(url='http://hpiers.obspm.fr/'))

HPIERS_OBSPM_FR_FTP = Misc.generic(cite_key='hpiers_obspm_fr_ftp',
                                   crossref=OBSPM,
                                   non_standard=NonStandard(url='ftp://hpiers.obspm.fr/'))

MATHEWS_AL_2002 = Article.generic(cite_key='mathews_al_2002',
                                  author='',
                                  crossref=JOURNAL_GEOPHYSICAL_RESEARCH,
                                  note='https://agupubs.onlinelibrary.wiley.com/doi/epdf/10.1029/2001JB000390',
                                  title="Modeling of nutation and precession: New nutation series for nonrigid Earth and insights into the Earth's interior",
                                  volume='107',
                                  year=2002,
                                  non_standard=NonStandard(url='https://ui.adsabs.harvard.edu/abs/2002JGRB..107.2068M/abstract'))

MHB2000 = Misc.generic(cite_key='mhb2000',
                       crossref=MATHEWS_AL_2002,
                       title='MHB2000 nutation model',
                       non_standard=NonStandard(url='http://www-gpsg.mit.edu/~tah/mhb2000/'))

RENATO_2007 = Misc.generic(cite_key='renato_2007',
                           title='Third-Body Perturbation Using a Single Averaged Model: Application in Nonsingular Variables',
                           year=2007,
                           non_standard=NonStandard(url='https://pdfs.semanticscholar.org/f952/eeea55dd380d86e01c131d249758c8c2b151.pdf'))

IAU_2006_B1 = TechReport.generic(cite_key='iau_2006_b1',
                                 author='',
                                 crossref=IAU,
                                 number='IAU 2006 Resolution B1',
                                 title='Adoption of the P03 Precession Theory and Definition of the Ecliptic',
                                 type='recommendation',
                                 year=2006,
                                 non_standard=NonStandard(url='https://www.iau.org/static/resolutions/IAU2006_Resol1.pdf'))

IERS_TN_36 = TechReport.generic(cite_key='iers_tn_36',
                                author='',
                                crossref=IERS,
                                number='IERS Technical Note No. 36',
                                title='IERS Conventions (2010)',
                                type='document',
                                year=2010,
                                non_standard=NonStandard(url='https://www.iers.org/IERS/EN/Publications/TechnicalNotes/tn36.html'))

WKT_CRS_V1_0 = TechReport.generic(cite_key='wkt_crs_v1_0',
                                  author='',
                                  crossref=OGC,
                                  month='May',
                                  number='OGC 12-063r5',
                                  title='Geographic information - Well known text representation of coordinate reference systems',
                                  type='standard',
                                  year=2015,
                                  non_standard=NonStandard(url='http://docs.opengeospatial.org/is/12-063r5/12-063r5.html'))

WKT_CRS_V2_0_6 = TechReport.generic(cite_key='wkt_crs_v2_0_6',
                                    author='',
                                    crossref=OGC,
                                    month='August',
                                    number='OGC 18-010r7',
                                    title='Geographic information - Well known text representation of coordinate reference systems',
                                    type='standard',
                                    year=2019,
                                    non_standard=NonStandard(url='http://docs.opengeospatial.org/is/18-010r7/18-010r7.html'))

FITS_V4_0 = TechReport.generic(cite_key='fits_v4_0',
                               author='',
                               crossref=IAU,
                               month='July',
                               title='Definition of the Flexible Image Transport System (FITS)',
                               type='standard',
                               year=2016)

WMO_CODES_2_2019 = TechReport.generic(cite_key='wmo_codes_2_2019',
                                      author='',
                                      crossref=WMO,
                                      title='Manual on Codes - International Codes, Volume I.2, Annex II to the WMO Technical Regulations: Part B – Binary Codes, Part C – Common Features to Binary and Alphanumeric Codes',
                                      type='standard',
                                      year=2019)

OBJECT_MODEL_FOR_INTEROPERABLE_GEOPROCESSING = TechReport.generic(cite_key='object_model_for_interoperable_geoprocessing',
                                                                  author='',
                                                                  crossref=OGC,
                                                                  number='96-015R1',
                                                                  title='The OpenGis Abstract Specification: An Object Model for Interoperable Geoprocessing, Revision 1',
                                                                  type='specification',
                                                                  year=1996)

FILTER_1_1_0 = TechReport.generic(cite_key='filter_1_1_0',
                                  author='',
                                  crossref=OGC,
                                  number='OGC 04-095',
                                  title='OpenGIS Filter Encoding Implementation Specification',
                                  type='specification',
                                  year=2005,
                                  non_standard=NonStandard(url='http://portal.opengeospatial.org/files/?artifact_id=8340'))

CSW_1_1_1 = TechReport.generic(cite_key='csw_1_1_1',
                               author='',
                               crossref=OGC,
                               number='OGC 02-087r3',
                               title='OpenGIS Catalog Services Specification',
                               type='specification',
                               year=2002)

GEOTIFF_1_1 = TechReport.generic(cite_key='geotiff_1_1',
                                 author='',
                                 crossref=OGC,
                                 number='19-008r4',
                                 title='OGC GeoTIFF Standard',
                                 type='standard',
                                 year=1992,
                                 non_standard=NonStandard(url='http://docs.opengeospatial.org/is/19-008r4/19-008r4.html'))

TIFF_V6 = TechReport.generic(cite_key='tiff_v6',
                             author='',
                             institution='',
                             title='TIFF Revision 6.0',
                             type='document',
                             year=1992,
                             non_standard=NonStandard(url='https://www.adobe.io/open/standards/TIFF.html'))

PNG_V3 = TechReport.generic(cite_key='png_v3',
                            author='',
                            crossref=W3C,
                            title='Portable Network Graphics (PNG) Specification (Third Edition)',
                            type='recommendation',
                            year=2022,
                            non_standard=NonStandard(url='https://www.w3.org/TR/png/'))

NETCDF_APPENDIX_B = TechReport.generic(cite_key='netcdf_appendix_b',
                                       author='',
                                       crossref=UCAR,
                                       title='Appendix B. File Format Specifications',
                                       type='specification',
                                       year=2018,
                                       non_standard=NonStandard(url='https://docs.unidata.ucar.edu/netcdf-c/current/file_format_specifications.html'))

FUKUSHIMA_1991 = Article.generic(cite_key='fukushima_1991',
                                 author='',
                                 crossref=ASTRONOMY_ASTROPHYSICS,
                                 title='Geodesic nutation',
                                 volume='244',
                                 year=1991,
                                 non_standard=NonStandard(url='https://ui.adsabs.harvard.edu/abs/1991A%26A...244L..11F/abstract'))

LASKAR_1993 = Article.generic(cite_key='laskar_1993',
                              author='',
                              crossref=ASTRONOMY_ASTROPHYSICS,
                              pages='522-533',
                              title='Orbital, precessional, and insolation quantities for the Earth from -20 MYR to +10 MYR',
                              volume='270',
                              year=1993,
                              non_standard=NonStandard(url='http://adsabs.harvard.edu/abs/1993A&A...270..522L'))

SIMON_AL_1994 = Article.generic(cite_key='simon_al_1994',
                                author='',
                                crossref=ASTRONOMY_ASTROPHYSICS,
                                pages='663-683',
                                title='Numerical Expressions for precession formulae and mean elements for the Moon and the planets',
                                volume='282',
                                year=1994,
                                non_standard=NonStandard(url='http://adsabs.harvard.edu/abs/1994A%26A...282..663S'))

SOUCHAY_AL_1999 = Article.generic(cite_key='souchay_al_1999',
                                  author='',
                                  crossref=ASTRONOMY_ASTROPHYSICS_SUPPL_SERIES,
                                  pages='111-131',
                                  title='Corrections and new developments in rigid earth nutation theoryIII. Final tables \"REN-2000\" including crossed-nutation and spin-orbit coupling effects',
                                  volume='135',
                                  year=1999,
                                  non_standard=NonStandard(url='https://www.researchgate.net/profile/Marta_Folgueira/publication/228793411_Corrections_and_new_developments_in_rigid_earth_nutation_theory_III_Final_tables_REN-2000_including_crossed-nutation_and_spin-orbit_coupling_effects/links/558bda4608ae40781c1f1d06.pdf'))

CAPITAINE_AL_2003 = Article.generic(cite_key='capitaine_al_2003',
                                    author='',
                                    crossref=ASTRONOMY_ASTROPHYSICS,
                                    title='Expressions for IAU 2000 precession quantities',
                                    volume='412',
                                    year=2003,
                                    non_standard=NonStandard(url='https://www.aanda.org/articles/aa/pdf/2003/48/aa4068.pdf'))

BRETAGNON_AL_2003 = Article.generic(cite_key='bretagnon_al_2003',
                                    author='',
                                    crossref=ASTRONOMY_ASTROPHYSICS,
                                    note='subtitle: Considerations about the ecliptic and the Earth Orientation Parameters',
                                    title='Expressions for precession consistent with the IAU 2000A model',
                                    volume='400',
                                    year=2003,
                                    non_standard=NonStandard(url='https://www.aanda.org/articles/aa/pdf/2003/11/aa2753.pdf'))

LASKAR_2004 = Article.generic(cite_key='laskar_2004',
                              author='',
                              crossref=ASTRONOMY_ASTROPHYSICS,
                              pages='261-285',
                              title='A long-term numerical solution for the insolation quantities of the Earth',
                              volume='428',
                              year=2004,
                              non_standard=NonStandard(url='https://www.aanda.org/articles/aa/pdf/2004/46/aa1335.pdf'))

CAPITAINE_AL_2005 = Article.generic(cite_key='capitaine_al_2005',
                                    author='',
                                    crossref=ASTRONOMY_ASTROPHYSICS,
                                    pages='355-367',
                                    title='Improvement of the IAU 2000 precession model',
                                    volume='432',
                                    year=2005,
                                    non_standard=NonStandard(url='https://www.aanda.org/articles/aa/pdf/2005/10/aa1908.pdf'))

WALLACE_AL_2006 = Article.generic(cite_key='wallace_al_2006',
                                  author='',
                                  crossref=ASTRONOMY_ASTROPHYSICS,
                                  pages='981-987',
                                  title='Precession-nutation procedures consistent with IAU 2006 resolutions',
                                  volume='459',
                                  year=2006,
                                  non_standard=NonStandard(url='https://www.aanda.org/articles/aa/pdf/2006/45/aa5897-06.pdf'))
