foreach pdb [glob models/*.final.pdb] {
    mol new $pdb
    mol modstyle 0 top NewCartoon
    mol modcolor 0 top ColorID [molinfo top get id]
}
