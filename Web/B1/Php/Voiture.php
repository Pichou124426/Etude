<?php
class Voiture
{
    protected $brand;
    protected $model;
    protected $year;

    function getBrand()
    {
        return $this->brand;
    }
    function getModel()
    {
        return $this->model;
    }
    function getYear()
    {
        return $this->year;
    }

    function setBrand($brand)
    {
        $this->brand = $brand;
    }
    function setModel($model)
    {
        $this->model = $model;
    }
    function setYear($year)
    {
        $this->year = $year;
    }
}

class VoitureElectrique extends Voiture
{
    private $autonomie;
    public function setAutonomie($autonomie)
    {
        $this->autonomie = $autonomie;
    }
    public function getAutonomie()
    {
        return $this->autonomie;
    }
}





$noah = new Voiture();
$clio = new VoitureElectrique();

$clio->setBrand('Peugeot');
$clio->setModel('208');
$clio->setYear('2024');
$clio->setAutonomie('65');

echo "La marque du véhicule est ";
echo $clio->getBrand();
echo ".<br>";
echo "Le modele du véhicule est ";
echo $clio->getModel();
echo ".<br>";
echo "L'année du véhicule est ";
echo $clio->getYear();
echo ".<br>";
echo "L'autominie restante du véhicule est ";
echo $clio->getAutonomie();
echo "%.<br>";
