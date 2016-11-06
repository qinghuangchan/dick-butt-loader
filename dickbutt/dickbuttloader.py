import sys
import time
import math

def demo(number_of_iterations=100):

    print('Introducing....\n')
    time.sleep(2)
    print('The Dick Butt Loading Screen\n')

    time.sleep(2)

    print('Ready?\n\n')

    time.sleep(2)

    print('LOAD!!!!')

    time.sleep(1)

    sample_iterator = ['example'] * number_of_iterations

    count = 0
    total = len(sample_iterator)

    for _ in sample_iterator:

        # add these two lines within loop
        progress_dick_butt(count, total)
        count = count + 1

        # do other code
        time.sleep(0.05)

def progress_dick_butt(iteration_count, total):
    bar_len = len(loader_text)
    filled_len = int(bar_len * (iteration_count + 1) / float(total))
    filled_len_prev = int(bar_len * (iteration_count) / float(total))

    percents = 100.0 * (iteration_count + 1) / float(total)
    bar = '=' * filled_len + '-' * (bar_len - 1 - filled_len)

    # prev_line = int(filled_len - 1)
    # this_line = int(filled_len)

    while filled_len > filled_len_prev:
        filled_len_prev = filled_len_prev + 1
        sys.stdout.write('%s\n' % loader_text[filled_len_prev - 1])

    sys.stdout.write('      [%s] %s%s ...\r' % (bar, percents, '%'))
    sys.stdout.flush()  # As suggested by Rom Ruben



loader_text  = ['                                                                                          ',
                '                                      DiCkBuTtD                                           ',
                '                                  1ckbu++D!ckBu+tDi                                       ',
                '                              CkBuTtD1ckbu++D!ckBu+tDi                                    ',
                '                      CkBuTtD1ckbu++D           !ckBu+tD                                  ',
                '                   iCkBuTtD1ckbu                  ++D!ckB                                 ',
                '                 u+tDiCkBuTtD1ck                   bu++D!                                 ',
                '                 ckBu+tDiCkBuTtD1                   ckbu+                                 ',
                '                 +D!ckBu+tDi CkBuTt    D1ckbu++D!c  kBu+t                                 ',
                '                 DiCkBuTtD1ckbu++D!c kBu+tDiCkBuTtD1 ckbu                                 ',
                '                 ++D!ckBu+tDiCkBuT  tD1ckbu++D!ckBu+tDiCk                                 ',
                '                BuTtD  1ckbu++D!ck  Bu+tDiCkBuTtD1ckbu++D                                 ',
                '               !ckBu+tDiCkBuTtD1ckb u++D!ckBu+t DiCkBuTtD                                 ',
                '              1ckbu++D!ckBu+tDiCk   BuTtD1ckbu++D!ckBu+tD                                 ',
                '             iCkBuTtD1ckbu++D!ckBu+tDiCkBuTtD1ckb  u++D!                                  ',
                '            ckBu+          tDiCkBuTtD1ckbu++D     !ckBu+                                  ',
                '           tDiCk                      BuTtD1c     kbu++D                                  ',
                '          !ckBu+                                 tDiCkB                                   ',
                '         uTtD1c                                 kbu++D                                    ',
                '        !ckBu+                                  tDiCkB                                    ',
                '        uTtD1                      ckbu        ++D!ck                                     ',
                '        Bu+t                      DiCkB uTt   D1ckbu                                      ',
                '        ++D!                      ckBu+tDiCk  BuTtD                         1ckbu++D!     ',
                '       ckBu+                      tDiCkBuTt  D1ckb                        u++D!ckBu+tD    ',
                '       iCkBu                     TtD1ckbu++ D!ckB                       u+tDiC    kBuT    ',
                '       tD1ck                     bu++D!ckB  u+tDi                     CkBuTtD    1ckbu    ',
                '       ++D!c                    kBu+tDiCk  BuTtD1                   ckbu++D     !ckBu     ',
                '       +tDiC                    kBuTtD1c   kbu++D!ckBu+tDiCkBuT   tD1ckbu     ++D!c       ',
                '        kBu+                   tDiCkBuT    tD1ckbu++D!ckBu+tDiCkBuTtD1c      kbu++        ',
                '        D!ck                   Bu+tDiC     kBuTt   D1ckb   u++D!ckBu+      tDiCkB         ',
                '        uTtD                  1ckbu++D      !ck   Bu+tDiCkBuTtD1ckb      u++D!c           ',
                '        kBu+t               DiCkB uTtD1         ckbu++D!ckBu+tDiCk     BuTtD1c            ',
                '         kbu+             +D!ck  Bu+tDiC         kBuTtD1ckbu++D!ckBu   +tDiCkBu           ',
                '         TtD1c            kbu++D!ckBu+tD                     iCkBuTtD    1ckbu++D!        ',
                '          ckBu+            tDiCkBuTtD1c              kbu+       +D!ckB  u+tD iCkBu        ',
                '          TtD1ck              bu++                   D!ck        Bu+tDi  CkBuTtD1         ',
                '           ckbu++                                D!c              kBu+t    DiCk           ',
                '            BuTtD1ck                            bu++              D!ckB     u+tD          ',
                '               iCkBuTt                          D1ck              bu++D!ckBu+tDi          ',
                '     CkB        uTtD1ckbu+                       +D!c           kBu+tDiCkBuTtD1           ',
                '    ckbu++D    !ckBu+tDiCkBuTtD1                  ckb         u++D!ck    B                ',
                '    u+tDiCkBuTtD1c kbu++D!ckBu+tDiCkBuTt           D1ck    bu++D!c                        ',
                '    kBu+ tDiCkBuTtD1ckb    u++D!ckBu+tDiCk BuTtD1ckbu++D!ckBu+tD                          ',
                '     iCkB  uTtD1ckbu+         +D!ckBu+tDi CkBuTtD1ckbu++D!ckB                             ',
                '      u+tD   iCkBuT         tD1ckbu++D!c kBu+t DiCkBuTtD1c                                ',
                '       kbu++D!ckB           u+tDiCkBuTt  D1ck                                             ',
                '        bu++D!c              kBu+tDiC   kBuT                                              ',
                '          tD1                ckbu++    D!ck                                               ',
                '                              Bu+tDi  CkBu                                                ',
                '                               TtD1ckbu++                                                 ',
                '                                 D!ckBu+                                                  ',
                '                                   tDi                                                    '
                '                                                                                          ',
                '                                                                                          ',
                '                                                                                          ',
                '                  _____ _____ _____ _  ______  _    _ _______ _______                     ',
                '                 |  __ \_   _/ ____| |/ /  _ \| |  | |__   __|__   __|                    ',
                '                 | |  | || || |    | \' /| |_) | |  | |  | |     | |                       ',
                '                 | |  | || || |    |  < |  _ <| |  | |  | |     | |                       ',
                '                 | |__| || || |____| . \| |_) | |__| |  | |     | |                       ',
                '                 |_____/_____\_____|_|\_\____/ \____/   |_|     |_|                       ',
                '                                                                                          ',]


