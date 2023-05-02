.. Virtual Brain Lab documentation master file, created by
.. sphinx-quickstart on Wed Jun  8 16:18:12 2022.
.. You can adapt this file completely to your liking, but it should at least
.. contain the root `toctree` directive.

.. image:: https://github.com/VirtualBrainLab/.github/raw/main/images/brain_text-01.png
  :width: 650
  :alt: logo

=================

Virtual Brain Lab
==================

The VBL builds intuitive and interactive 3D visualizations for neuroscience.

We are located within the `Steinmetz Lab <http://steinmetzlab.net>`_ at the University of Washington and many of our projects are collaborations with the `International Brain Laboratory <https://www.internationalbrainlab.com>`_.

.. |image1| image:: ./_static/images/steinmetz_lab.jpg
   :width: 30%

.. |image2| image:: ./_static/images/ibl_lab.png
   :width: 30%

.. raw:: html

   <div style="display:flex;">
   <div style="flex:1;margin-right:5px;">
   |image1|
   </div>
   <div style="flex:1;margin-left:5px;">
   |image2|
   </div>
   </div>

Please see the individual projects for installation instructions and documentation. You can find all our code on `Github <https://github.com/VirtualBrainLab>`_.

.. toctree::
   :hidden:
   :maxdepth: 2
   :caption: Pinpoint

   pinpoint/installation_and_use
   pinpoint/tutorial
   pinpoint/in_vivo_alignment

.. toctree::
   :hidden:
   :maxdepth: 2
   :caption: Urchin

   urchin/installation_and_use
   ibl/ibl_tools

.. toctree::
   :hidden:
   :maxdepth: 2
   :caption: Ephys Link

   ephys_link/installation_and_use

.. toctree::
   :hidden:
   :maxdepth: 3
   :caption: Development

   pinpoint/development
   urchin/development
   ephys_link/development

.. toctree::
   :hidden:
   :maxdepth: 2
   :caption: Misc

   misc/brain_atlas

.. toctree::
   :hidden:
   :maxdepth: 2
   :caption: About the VBL

   about/overview
   about/vbl_manual
   about/contract_us

.. toctree::
   :hidden:
   :caption: API Reference
   :maxdepth: 1

   api_reference_urn.rst
   api_reference_ephys_link.rst